# Configuration
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


# Class
class Restaurant(Base):
    # Table
    __tablename__ = 'restaurant'
    # Mapper
    id = Column(Integer,
                primary_key=True)
    name = Column(String(80), nullable=False)
    address = Column(String(250), nullable=False)


# Class
class MenuItem(Base):
    # Table
    __tablename__ = 'menu_item'
    # Mapper
    id = Column(Integer,
                primary_key=True)
    name = Column(String(80),
                  nullable=False)
    course = Column(String(250))
    description = Column(String(250))
    price = Column(String(8))
    restaurant_id = Column(Integer,
                           ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    # this property is from MenuItem
    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'course': self.course
        }


engine = create_engine('sqlite:///restaurant.db')

Base.metadata.create_all(engine)
__author__ = 'aungthiha'
