from sqlalchemy.orm import Session
from src.schemas import schemas
from sqlalchemy import select
from src.infra.sqlalchemy.models import models

class UserRepository():

    def __init__(self, session: Session):
        self.session = session

    def create(self, user: schemas.User):
        db_user = models.User(
            name = user.name,
            phone_number = user.phone_number,
            password = user.password
        )
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def get_user_by_phone_number(self, phone_number : str):
        query = select(models.User).where(models.User.phone_number == phone_number)
        user = self.session.execute(query).scalars().first()
        return user

    def remove_user(self):
        pass