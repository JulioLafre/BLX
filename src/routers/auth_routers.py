from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from src.schemas.schemas import User, SimpleUser, LoginData
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.users import UserRepository
from src.infra.providers import hash_provider, token_provider

router = APIRouter()

@router.post("/signup", status_code=status.HTTP_201_CREATED, response_model=SimpleUser)
def signup(user: User, db: Session = Depends(get_db)):
    #Checking if the user already exists
    located_user = UserRepository(db).get_user_by_phone_number(user.phone_number)
    if located_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="There is already a user with this phone number.")

    user.password = hash_provider.create_hash(user.password)
    user_create = UserRepository(db).create(user)
    return user_create

@router.post("/signin")
def signin(login_data: LoginData, db: Session = Depends(get_db)):
    password = login_data.password
    phone_number = login_data.phone_number
    user = UserRepository(db).get_user_by_phone_number(phone_number)

    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="User or Phone Number don't exist")
    
    valid_password = hash_provider.verify_hash(password, user.password)

    if not valid_password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, 
                            detail="User or Phone Number don't exist")
    
    token = token_provider.create_access_token({"sub": phone_number})
    return {"access_token": token}

@router.get("/me")
def me(token: str, db: Session = Depends(get_db)):
    pass
