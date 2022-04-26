from models.laptop_model import LaptopModel
from sqlalchemy.orm.session import Session


class LaptopDao:
    def __init__(self, session: Session):
        self.__session = session

    def get_all_laptop(self):
        return self.__session.query(LaptopModel).all()
