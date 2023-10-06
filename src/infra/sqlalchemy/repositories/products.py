from sqlalchemy.orm import Session
from sqlalchemy import update, delete
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
            available = product.available,
            user_id = product.user_id
            )
        self.session.add(db_product)
        self.session.commit()
        self.session.refresh(db_product)
        return db_product


    def list(self):
        products = self.session.query(models.Product).all()
        return products


    def edit_product(self, product: schemas.Product):
        update_stmt = update(models.Product)\
        .where(models.Product.product_id == product.product_id)\
        .values(
            name = product.name,
            details = product.details,
            price = product.price,
            available = product.available,
            user_id = product.user_id
            )

        self.session.execute(update_stmt)
        self.session.commit()


    def get_product(self):
        pass


    def delete_product(self, id: int):
        delete_stmt = delete(models.Product)\
                      .where(models.Product.product_id == id)
        self.session.execute(delete_stmt)
        self.session.commit()

