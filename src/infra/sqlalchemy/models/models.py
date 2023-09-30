from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from src.infra.sqlalchemy.config.database import Base

class Product(Base):

    __tablename__ = "Products"
    
    _id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    user = Column(Integer, ForeignKey("users._id", ondelete="CASCADE"),nullable=False)
    details = Column(String, nullable=True)
    price = Column(Float, nullable=False)
    available = Column(Boolean, server_default=False)

class User(Base):

    __tablename__ = "users"

    _id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=True)
