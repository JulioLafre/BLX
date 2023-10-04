from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    _id: Optional[int] = None
    name: str
    phone_number: str
    my_products: List['Product'] = []
    my_sales: List['Order'] = []
    my_purchases: List['Order'] = []

    class Config:
        orm_mode = True

class SimpleUser(BaseModel):
    name: str

    class Config:
        orm_mode = True

class SimpeProduct(BaseModel):
    name: str
    price: float

    class Config:
        orm_mode = True

class Product(BaseModel):
    _id: Optional[int] = None
    name: str
    details: str
    price: float
    available: bool = True 

    class Config:
        orm_mode = True

class Order(BaseModel):
    _id: Optional[int] = None
    user: User
    product: Product
    amount: int
    delivered: bool = False
    local: str
    obs: Optional[str] = "no comments"