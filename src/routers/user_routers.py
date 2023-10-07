from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from src.schemas.schemas import User,SimpleUser
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.users import UserRepository

router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=SimpleUser)
def signup(user: User, db: Session = Depends(get_db)):
    user_create = UserRepository(db).create(user)
    return user_create


@router.get("/users", response_model=List[User])
def users_list(db: Session = Depends(get_db)):
    users = UserRepository(db).list()
    return users
