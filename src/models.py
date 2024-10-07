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

class Population(Base):
    __tablename__ = 'population'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True) 
    name   = Column(String(100)) 
    diameter = Column(Integer)
    climate = Column(String(50))

class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    film_id = Column(Integer, ForeignKey('film.id'))

class Film(Base):
    __tablename__ = 'film'
    id = Column(Integer, primary_key=True)    
    title  = Column(String(100))
    episode_id = Column(Integer)





    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
