from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from src.schemas.schemas import Product,SimpleProduct,UpdateProduct,GetProduct 
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.products import ProductRepository


router = APIRouter()


@router.delete("/products/{id}")
def remove_product(id: int, db: Session = Depends(get_db)):
    product_removed = ProductRepository(db).delete_product(id)
    return product_removed


@router.put("/products/{id}", response_model=GetProduct)
def update_product(id: int, product: UpdateProduct, db: Session = Depends(get_db)):
    product_updated = ProductRepository(db).edit_product(id, product)
    return product_updated


@router.post("/products", status_code=status.HTTP_201_CREATED, response_model=SimpleProduct)
def create_product(product: Product, db: Session = Depends(get_db)):
    product_created = ProductRepository(db).create(product)
    return product_created


@router.get("/products", response_model=List[Product])
def products_list(db: Session = Depends(get_db)):
    products = ProductRepository(db).list()
    return products


@router.get("/products/{id}")
def get_product(id: int, db: Session = Depends(get_db)):
    product = ProductRepository(db).get_product_by_id(id)
    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="non-existent product")
    return product