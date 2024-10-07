import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

'''class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)'''

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)    
    first_name   = Column(String(100)) 
    last_name   = Column(String(150)) 
    user_name   = Column(String(150)) 
    password = Column(String(150))
    email = Column(String(150))

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('user.id'))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)    
    birth_year = Column(String(20))
    eye_color = Column(String(50))
    gender = Column(String(50))
    hair_color  = Column(String(50))
    height = Column(Integer)
    mass   = Column(Integer) 
    name   = Column(String(100)) 
    skin_color = Column(String(50))
    created = Column(String(80))
    edited  = Column(String(80))
    character_id = Column(Integer, ForeignKey('planet.id'))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True) 
    name   = Column(String(100)) 
    diameter = Column(Integer)
    climate = Column(String(50))






    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
