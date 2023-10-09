from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import Relationship 
from src.infra.sqlalchemy.config.database import Base

class Product(Base):

    __tablename__ = "products"
    
    product_id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    available = Column(Boolean, server_default="true")
    user_id = Column(Integer,ForeignKey("users.user_id", name="fk_user_product"))
    user = Relationship("User", back_populates="products")


class User(Base):

    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    phone_number = Column(String)
    password = Column(String)
    products = Relationship("Product", back_populates="user")

class Order(Base):

    __tablename__ = "orders"

    order_id = Column(Integer, primary_key=True, index=True, nullable=False)
    quantity = Column(Integer),
    delivery_adress = Column(str),
    delivery_type = Column(str),
    note = Column(str),
    user_id = Column(Integer,ForeignKey(
        "users.user_id", name="fk_user_order")),
    product_id = Column(Integer,ForeignKey(
        "product.product_id", name="fk_product_order"))
    user = Relationship("User", back_populates="orders")
    products = Relationship("Product", back_populates="orders")
    

