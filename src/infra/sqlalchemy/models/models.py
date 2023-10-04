from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import Relationship 
from src.infra.sqlalchemy.config.database import Base

class Product(Base):

    __tablename__ = "products"
    
    _id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String)
    details = Column(String)
    price = Column(Float)
    available = Column(Boolean, server_default="true")
    user_id = Column(Integer,ForeignKey("users._id", name="fk_usuario"))
    user = Relationship("User", back_populates="products")


class User(Base):

    __tablename__ = "users"

    _id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    phone_number = Column(String)
    products = Relationship("Product", back_populates="user")