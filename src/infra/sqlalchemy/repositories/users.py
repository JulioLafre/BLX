from sqlalchemy.orm import Session
from src.schemas import schemas
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
    
    def list(self):
        users = self.session.query(models.User).all()
        return users

    def get_user(self):
        pass

    def remove_user(self):
        pass