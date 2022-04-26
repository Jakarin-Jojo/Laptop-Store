from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utilities.dao.customer_dao import CustomerDao
from utilities.dao.laptop_dao import LaptopDao


class LaptopDB:

    def __init__(self):
        self.__engine = create_engine('sqlite:///laptop_store.db', echo=True)
        session = sessionmaker(bind=self.__engine)
        self.__session = session()

    def customer(self):
        return CustomerDao(self.__session)

    def laptop(self):
        return LaptopDao(self.__session)
