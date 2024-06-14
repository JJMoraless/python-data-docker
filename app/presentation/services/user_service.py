from sqlalchemy.orm import Session


from ...data.models.user import UserModel
from ...data.models.email_acount import EmailAccountModel


class UserService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.email_acount = db.query(EmailAccountModel)
        self.user = db.query(UserModel)

    def get_user_by_id(self, user_id: int) -> UserModel:
        return self.user.filter(UserModel.id == user_id).first()
