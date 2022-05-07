from models.laptop_model import LaptopModel
from sqlalchemy.orm.session import Session


class LaptopDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_laptop(self):
        return self.__session.query(LaptopModel).all()

    def get_laptop_by_id(self, id):
        return self.__session.query(LaptopModel).filter_by(id=id)[0]

    def get_laptop_price_less_than_or_equal(self, price: int):
        return self.__session.query(LaptopModel).filter(LaptopModel.price_euros <= price).all()

    def get_laptop_price_more_than_or_equal(self, price: int):
        return self.__session.query(LaptopModel).filter(LaptopModel.price_euros >= price).all()

    def get_laptop_by_type_name(self, type_name):
        return self.__session.query(LaptopModel).filter(LaptopModel.type_name == type_name).all()

    def add_new_customer(self, laptop):
        self.__session.add(laptop)
        self.__session.commit()
        print(f"{laptop.product} is added in the database")
