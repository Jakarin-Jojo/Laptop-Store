from sqlalchemy import Column, Integer, Text, FLOAT
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class LaptopModel(Base):
    __tablename__ = "laptop"
    id = Column(Integer, primary_key=True)
    company = Column(Text, nullable=False)
    product = Column(Text, nullable=False)
    type_name = Column(Text, nullable=False)
    screen_size_inches = Column(FLOAT, nullable=False)
    screen_resolution = Column(Text, nullable=False)
    ram = Column(Text, nullable=False)
    memory = Column(Text, nullable=False)
    GPU = Column(Text, nullable=False)
    operating_system = Column(Text, nullable=False)
    weight = Column(Text, nullable=False)
    price_euros = Column(FLOAT, nullable=False)

    def __repr__(self):
        return f"Laptop(id = {self.id}, company = {self.company}, product = {self.product}, type_name = {self.type_name}), "\
            f"screen_size_inches = {self.screen_size_inches}, screen_resolution = {self.screen_resolution}, ram = {self.ram}, "\
            f"memory = {self.memory}, GPU = {self.GPU}, operating_system = {self.operating_system}, weight = {self.weight}, "\
            f"price_euros = {self.price_euros}"
