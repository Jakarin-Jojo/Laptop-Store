from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utilities.dao.customer_dao import CustomerDao
from utilities.dao.laptop_dao import LaptopDao


class LaptopDB:

    def __init__(self):
        engine = create_engine('sqlite:///laptop_store.db', echo=True)
        session = sessionmaker(bind=engine)
        self.__session = session()

    def customer(self):
        return CustomerDao(self.__session)

    def laptop(self):
        return LaptopDao(self.__session)
