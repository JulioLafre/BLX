from fastapi import APIRouter, Depends, status
from typing import List
from sqlalchemy.orm import Session
from src.schemas.schemas import Order
from src.infra.sqlalchemy.config.database import get_db
from src.infra.sqlalchemy.repositories.orders import OrderRepository


router = APIRouter()

@router.post("/orders", status_code=status.HTTP_201_CREATED)
def create_order(order: Order, db: Session = Depends(get_db)):
    order_created = OrderRepository(db).create(order)
    return order_created

@router.get("/orders/{id}", response_model=Order)
def get_user_order(id: int, db: Session = Depends(get_db)):
    order = OrderRepository(db).display_order(id)
    return order

@router.get("/orders/{user_id}", response_model=List[Order])
def get_user_list_order(user_id: int, db: Session = Depends(get_db)):
    orders_list = OrderRepository(db).get_orders_by_user_id(user_id)
    return orders_list

@router.get("/sales/{user_id}/vendas", response_model=List[Order])
def get_user_list_sales(user_id: int, db: Session = Depends(get_db)):
    sales_list = OrderRepository(db).get_sales_by_user_id(user_id)
    return sales_list