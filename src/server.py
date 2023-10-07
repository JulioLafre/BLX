from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from src.schemas.schemas import Product,User,SimpleProduct,SimpleUser,UpdateProduct,\
GetProduct
from src.infra.sqlalchemy.config.database import create_db, get_db
from src.infra.sqlalchemy.repositories.products import ProductRepository
from src.infra.sqlalchemy.repositories.users import UserRepository

create_db()

app = FastAPI()

#Cors
origins = [
    "http://localhost:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credential= True,
     allow_methods=["*"],
    allow_headers=["*"]
)

#Users Rotes
@app.post("/signup", status_code=status.HTTP_201_CREATED, response_model=SimpleUser)
def signup(user: User, db: Session = Depends(get_db)):
    user_create = UserRepository(db).create(user)
    return user_create


@app.get("/users", response_model=List[User])
def users_list(db: Session = Depends(get_db)):
    users = UserRepository(db).list()
    return users

#Products Rotes
@app.delete("/products/{id}")
def remove_product(id: int, db: Session = Depends(get_db)):
    product_removed = ProductRepository(db).delete_product(id)
    return product_removed


@app.put("/products/{id}", response_model=GetProduct)
def update_product(id: int, product: UpdateProduct, db: Session = Depends(get_db)):
    product_updated = ProductRepository(db).edit_product(id, product)
    return product_updated


@app.post("/products", status_code=status.HTTP_201_CREATED, response_model=SimpleProduct)
def create_product(product: Product, db: Session = Depends(get_db)):
    product_created = ProductRepository(db).create(product)
    return product_created


@app.get("/products", response_model=List[Product])
def products_list(db: Session = Depends(get_db)):
    products = ProductRepository(db).list()
    return products


@app.get("/products/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    product = ProductRepository(db).get_product_by_id(id)
    return product



