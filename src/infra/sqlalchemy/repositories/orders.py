from src.schemas import schemas
from sqlalchemy.orm import Session
from sqlalchemy import select
from src.infra.sqlalchemy.models import models

class OrderRepository():

    def __init__(self, session: Session):
        self.session = session


    def create(self, order: schemas.Order):
        db_order = models.Order(
            quantity = order.quantity,
            delivery_adress = order.delivery_adress,
            delivery_type = order.delivery_type,
            user_id = order.user_id,
            product_id = order.product_id
            )
        self.session.add(db_order)
        self.session.commit()
        self.session.refresh(db_order)
        return db_order



    def display_order(self, id: int):
        query = select(models.Order).where(models.Order.order_id == id)
        order = self.session.execute(query).scalars().first()
        return order


    def get_orders_by_user_id(self, user_id: int):
        query = select(models.Order).where(models.Order.user_id == user_id)
        order_list = self.session.execute(query).scalars().all()
        return order_list

    def get_sales_by_user_id(self, user_id: int):
        query = select(models.Order).join_from(models.Order, models.Product) \
        .where(models.Product.user_id == user_id)
        sales_list = self.session.execute(query).scalars().all()
        return sales_list