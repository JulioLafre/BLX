from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.schemas.schemas import User,SimpleUser
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.users import UserRepository
from src.infra.providers import hash_provider   

router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=SimpleUser)
def signup(user: User, db: Session = Depends(get_db)):
    #Checking if the user already exists
    located_user = UserRepository(db).get_user_by_phone_number(user.phone_number)
    if located_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="There is already a user with this phone number.")

    user.password = hash_provider.gerar_hash(user.password)
    user_create = UserRepository(db).create(user)
    return user_create
