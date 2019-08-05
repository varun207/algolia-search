from django.db import models
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import sqlalchemy

Base = declarative_base()
engine = sqlalchemy.create_engine('sqlite:///loose.sqlite')

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

class Products(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    model_number = Column(String)
    character = Column(String)
    brand = Column(String)
    description = Column(String(300))

    def __init__(self, name, model_number, character, brand, description):
        self.name = name
        self.model_number = model_number
        self.character = character
        self.brand = brand
        self.description = description


