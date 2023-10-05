from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from typing import List
from src.schemas.schemas import Product,User,SimpeProduct,SimpleUser
from src.infra.sqlalchemy.config.database import create_db, get_db
from src.infra.sqlalchemy.repositories.products import ProductRepository
from src.infra.sqlalchemy.repositories.users import UserRepository

create_db()

app = FastAPI()


#Users Rotes
@app.post("/users", status_code=status.HTTP_201_CREATED, response_model=SimpleUser)
def create_user(user: User, db: Session = Depends(get_db)):
    user_create = UserRepository(db).create(user)
    return user_create

@app.get("/users", response_model=List[User])
def users_list(db: Session = Depends(get_db)):
    users = UserRepository(db).list()
    return users

#Products Rotes
@app.put("/products")
def update_product(product: Product, db: Session = Depends(get_db)):
    product_updatated = ProductRepository(db).edit_product(product)
    return product_updatated

@app.post("/products", status_code=status.HTTP_201_CREATED, response_model=SimpeProduct)
def create_product(product: Product, db: Session = Depends(get_db)):
    product_created = ProductRepository(db).create(product)
    return product_created

@app.get("/products", response_model=List[Product])
def products_list(db: Session = Depends(get_db)):
    products = ProductRepository(db).list()
    return products



