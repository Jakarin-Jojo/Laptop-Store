from sqlalchemy import Column, Integer, Text
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CustomerModel(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True)
    firstname = Column(Text, nullable=False)
    lastname = Column(Text, nullable=False)
    gender = Column(Text, nullable=False)
    laptop_id = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Customer(id = {self.id}, firstname= {self.firstname}, lastname={self.lastname}, gender={self.gender},"\
               f" laptop_id ={self.laptop_id})> \n"
