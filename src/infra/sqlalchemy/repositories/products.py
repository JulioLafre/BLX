from sqlalchemy.orm import Session
from sqlalchemy import update, delete, select
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


    def edit_product(self, id: int, product: schemas.UpdateProduct):
        update_stmt = update(models.Product)\
        .where(models.Product.product_id == id)\
        .values(
            name = product.name,
            details = product.details,
            price = product.price,
            available = product.available,
            )

        self.session.execute(update_stmt)
        self.session.commit()
        return self.get_product_by_id(id)


    def get_product_by_id(self, id: int):
        query = select(models.Product).where(models.Product.product_id == id)
        product = self.session.execute(query).first()
        return product[0]


    def delete_product(self, id: int):
        delete_stmt = delete(models.Product)\
                      .where(models.Product.product_id == id)
        self.session.execute(delete_stmt)
        self.session.commit()

