from models.customer_model import CustomerModel
from sqlalchemy.orm.session import Session


class CustomerDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_customer(self):
        return self.__session.query(CustomerModel).all()

    def get_customer_by_id(self, id):
        return self.__session.query(CustomerModel).filter_by(id=id)[0]

    def add_new_customer(self, customer):
        self.__session.add(customer)
        self.__session.commit()
        print(f"{customer.firstname} is added in the database")
