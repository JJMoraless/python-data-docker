from sqlalchemy.orm import Session

import imaplib
import email
from email.header import decode_header


from ...data.models.email_acount import EmailAccountModel
from ...domain.schemas.email import EmailAcountSchema
from ...domain.errors.api_error import ApiError
import re
import os
from typing import List, Dict, Optional


class EmailService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.email_acount = db.query(EmailAccountModel)

    def save_email_acount(
        self, emailAcountSchema: EmailAcountSchema,
        user_id: int
    ) -> EmailAccountModel:

        email_acount_found = self.email_acount.filter(
            EmailAccountModel.email == emailAcountSchema.email
            and EmailAccountModel.user_id == user_id
        ).first()

        if email_acount_found:
            raise ApiError.bad_request("Email already registered")

        email_acount_schema = emailAcountSchema.model_dump()
        email_acount_schema["password"] = re.sub(
            r"\s", "", emailAcountSchema.password
        )

        email_acount = EmailAccountModel(
            **email_acount_schema,
            user_id=user_id,
        )

        self.db.add(email_acount)
        self.db.commit()
        return email_acount.to_dict()

    def get_email_acounts(self, user_id: int):
        email_acounts = self.email_acount.filter(
            EmailAccountModel.user_id == user_id
        ).all()
        return [email_acount.to_dict() for email_acount in email_acounts]

    # -----------  scanning emails ----------- #

    def connect_to_imap_server(
        server: str,
        user: str,
        password: str
    ) -> imaplib.IMAP4_SSL:

        imap = imaplib.IMAP4_SSL(server)
        imap.login(user, password)
        return imap

    def fetch_emails(
        self, imap: imaplib.IMAP4_SSL,
        folder: str = "INBOX",
        criteria: str = "ALL"
    ) -> List[bytes]:

        imap.select(folder)
        _, messages = imap.search(None, criteria)
        email_ids = messages[0].split()
        return email_ids

    def parse_email_subject(self, email_message: email.message.EmailMessage) -> str:
        subject, encoding = decode_header(email_message["Subject"])[0]

        if isinstance(subject, bytes):
            subject = subject.decode(encoding or "utf-8")

        return subject

    def save_attachment(
        part: email.message.EmailMessage,
        output_dir: str
    ) -> str | None:
        filename = part.get_filename()
        if filename and (filename.endswith(".xls") or filename.endswith(".xlsx")):
            os.makedirs(output_dir, exist_ok=True)
            filepath = os.path.join(output_dir, filename)

            with open(filepath, "wb") as f:
                f.write(part.get_payload(decode=True))

            return filepath

        return None

    def process_email(
        self,
        email_message: email.message.EmailMessage,
        output_dir: str
    ) -> Dict[str, Optional[str]]:
        
        sender = email_message.get("From")
        subject = self.parse_email_subject(email_message)
        email_info = {"remitente": sender, "asunto": subject}

        for part in email_message.walk():

            if "attachment" in str(part.get("Content-Disposition")):

                filepath = self.save_attachment(part, output_dir)
                if filepath:
                    email_info["adjunto"] = filepath

        return email_info

    def read_email(self, email_id: int):

        email_user = "jjmorales.dev@gmail.com"
        password = "ercutgejkentmwik"
        imap_server = "imap.gmail.com"
        output_dir = "excel_files"

        conection_imap = self.connect_to_imap_server(imap_server, email_user, password)
        email_ids = self.fetch_emails(conection_imap)

        emails = []
        for email_id in email_ids[-10:]:
            _, message = conection_imap.fetch(email_id, "(RFC822)")

            for response_part in message:

                if not isinstance(response_part, tuple):
                    continue

                email_message = email.message_from_bytes(response_part[1])
                email_info = self.process_email(email_message, output_dir)
                emails.append(email_info)

        conection_imap.logout()

        return emails
