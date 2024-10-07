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
    user_name   = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)    
    birth_year = Column(String(20), nullable=True)
    eye_color = Column(String(50), nullable=True)
    gender = Column(String(50), nullable=True)
    hair_color  = Column(String(50), nullable=True)
    height = Column(String(50), nullable=True)
    mass   = Column(String(50), nullable=True)
    name   = Column(String(100), nullable=True) 
    skin_color = Column(String(50), nullable=True)
    created = Column(String(80), nullable=True)
    edited  = Column(String(80), nullable=True)
    

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True) 
    name   = Column(String(100), nullable=True) 
    diameter = Column(String(100), nullable=True) 
    climate = Column(String(100), nullable=True) 
    population   = Column(String(100), nullable=True) 
    gravity = Column(String(100), nullable=True)
    terrain = Column(String(100), nullable=True)
    rotation_period = Column(String(100), nullable=True)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    name   = Column(String(100), nullable=False) 
    user_id = Column(Integer, ForeignKey('user.id'))
    user =  relationship(User)
    character_id = Column(Integer, ForeignKey('character.id'))
    character =  relationship(Character)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet =  relationship(Planet)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
