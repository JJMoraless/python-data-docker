from sqlalchemy.orm import Session


from ...data.models.user import UserModel
from ...data.models.email_acount import EmailAccountModel
from ...domain.schemas.user import UserSchema


class UserService:
    def __init__(self, db: Session) -> None:
        self.db = db
        self.email_acount = db.query(EmailAccountModel)
        self.user = db.query(UserModel)

    def get_user_by_id(self, user_id: int) -> UserModel:
        return self.user.filter(UserModel.id == user_id).first()

    def update_user(self, user_id: int, user_dto: UserSchema) -> UserModel:
        user_found = self.get_user_by_id(user_id)
        user_found.name = user_dto.name
        user_found.email = user_dto.email
        self.db.commit()
        return user_found.to_dict()
