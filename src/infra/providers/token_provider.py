from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "b5a2d9853948bd1618a50ae17bfdd047"
ALGORITHM = "HS256"
EXPIRES_IN_MIN = 30

def create_access_token(data: dict):
    pass

def verify_acess_token():
    pass