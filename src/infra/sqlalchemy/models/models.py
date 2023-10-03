from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from src.infra.sqlalchemy.config.database import Base

class Product(Base):

    __tablename__ = "products"
    
    _id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    details = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    available = Column(Boolean, nullable=False, server_default="true")


class User(Base):

    __tablename__ = "users"

    _id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    phone_number = Column(String, nullable=True)