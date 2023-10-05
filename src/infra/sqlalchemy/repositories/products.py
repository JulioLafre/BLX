from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

class ProductRepository():

    def __init__(self, session: Session):
        self.session = session

    def create(self, product: schemas.Product):
        db_product = models.Product(
            name = product.name,
            details = product.details,
            price = product.price,
            available = product.available
              )
        self.session.add(db_product)
        self.session.commit()
        self.session.refresh(db_product)
        return db_product

    def list(self):
        products = self.session.query(models.Product).all()
        return products

    def get_product(self):
        pass

    def remove_product(self):
        pass

