from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from src.schemas.schemas import Product, User
from src.infra.sqlalchemy.config.database import create_db, get_db
from src.infra.sqlalchemy.repositories.products import ProductRepository
from src.infra.sqlalchemy.repositories.users import UserRepository

create_db()

app = FastAPI()

@app.post("/profile")
def create_user(user: User, db: Session = Depends(get_db)):
    user_create = UserRepository(db).create(user)
    return {"Msg": f"Your user {user_create.name} has been created!"}

@app.get("/users")
def users_list(db: Session = Depends(get_db)):
    users = UserRepository(db).list()
    return users

@app.post("/products")
def create_product(product: Product, db: Session = Depends(get_db)):
    product_created = ProductRepository(db).create(product)
    return {"Msg": f"Your product {product_created.name} has been created!"}

@app.get("/products")
def products_list(db: Session = Depends(get_db)):
    products = ProductRepository(db).list()
    return products



