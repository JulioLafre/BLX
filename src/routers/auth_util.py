from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from sqlalchemy.orm import Session
from src.infra.sqlalchemy.config.database import get_db
from src.infra.providers import token_provider

oauth2_schema = OAuth2PasswordBearer(tokenUrl="token")

def get_loggedin_user(token: Depends(oauth2_schema)):
    pass
    