from pydantic import BaseModel
from typing import Optional, List

class User(BaseModel):
    user_id: Optional[int] = None
    name: str
    phone_number: str
    password: str
    my_products: List['Product'] = []
    my_sales: List['Order'] = []
    my_purchases: List['Order'] = []

    class Config:
        orm_mode = True

class SimpleUser(BaseModel):
    user_id: Optional[int] = None
    name: str
    phone_number: str

    class Config:
        orm_mode = True


class SimpleProduct(BaseModel):
    name: str
    details: str
    price: float
    available: bool

    class Config:
        orm_mode = True


class GetProduct(BaseModel):
    product_id: Optional[int] = None
    name: str
    details: str
    price: float
    available: bool = True
    user: Optional[User] = None

    class Config:
        orm_mode = True

class UpdateProduct(BaseModel):
    name: str
    details: str
    price: float
    available: bool = True

    class Config:
        orm_mode = True

class Product(BaseModel):
    product_id: Optional[int] = None
    name: str
    details: str
    price: float
    available: bool = True
    user_id: int
    user: Optional[User] = None

    class Config:
        orm_mode = True

class Order(BaseModel):
    order_id: Optional[int] = None
    user: User
    product: Product
    amount: int
    delivered: bool = False
    local: str
    obs: Optional[str] = "no comments"