from src.schemas import schemas
from sqlalchemy.orm import Session
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
            prodcut_id = order.product_id
            )
        self.session.add(db_order)
        self.session.commit()
        self.session.refresh(db_order)
        return db_order
    

    def display_order():
        pass


    def get_orders_by_user_id():
        pass


    def get_sales_by_user_id():
        pass