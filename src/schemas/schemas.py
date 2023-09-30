from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    _id: Optional[int] = None
    name: str
    phone_number: int
    my_products: List['Product'] = []
    my_sales: List['Order'] = []
    my_purchases: List['Order'] = []

class Product(BaseModel):
    _id: Optional[int] = None
    user: User
    name: str
    details: str
    price: float
    available: bool = False 

class Order(BaseModel):
    _id: Optional[int] = None
    user: User
    product: Product
    amount: int
    delivered: bool = False
    local: str
    obs: Optional[str] = "no comments"