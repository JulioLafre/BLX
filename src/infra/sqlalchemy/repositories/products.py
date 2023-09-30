from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class ProductRepository():

    def __init__(self, db: Session):
        self.db = db

    def create(self, product: schemas.Product):
        db_product = models.Product(
            name = product.name,
            user = product.user,
            details = product.details,
            price = product.price,
            available = product.available
              )
        self.db(db_product)
        self.db.commit()
        self.db.refresh(db_product)
        return db_product

    def list_products(self):
        products = self.db.query(models.Product).all()
        return products

    def get_product(self):
        pass

    def remove_product(self):
        pass

