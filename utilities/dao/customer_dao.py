from models.customer_model import CustomerModel
from sqlalchemy.orm.session import Session


class CustomerDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_customer(self):
        return self.__session.query(CustomerModel).all()