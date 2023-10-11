from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY = "b5a2d9853948bd1618a50ae17bfdd047"
ALGORITHM = "HS256"
EXPIRES_IN_MIN = 120

def create_access_token(data: dict):
    copied_data = data.copy()
    expiration = datetime.utcnow() + timedelta(minutes=EXPIRES_IN_MIN)

    copied_data.update({"exp": expiration})
    
    token_jwt = jwt.encode(copied_data, SECRET_KEY, algorithm=ALGORITHM)
    return token_jwt

def verify_access_token(token: str):
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload.get("sub")