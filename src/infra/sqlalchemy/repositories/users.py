from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class UserRepository():

    def __init__(self, db: Session):
        self.db = db

    def create(self, user: schemas.User):
        db_user = models.User(
            name = user.name,
            phone_number = user.phone_number
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
    
    def list(self):
        users = self.db.query(models.User).all()
        return users

    def get_user(self):
        pass

    def remove_user(self):
        pass