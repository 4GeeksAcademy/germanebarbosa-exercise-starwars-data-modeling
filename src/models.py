import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=True)
    user_name = Column(String(250), nullable=True)
    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet_name = Column(String(250))
    character_id = Column(Integer, ForeignKey('character.id'))
    character_name = Column(String(250))
    user = relationship(User)

class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True,nullable=True)
    planet_name = Column(String(250), nullable=True)
    population = Column(String(250))
    favorites = relationship(Favorites)

class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True,nullable=True)
    character_name = Column(String(250), nullable=True)
    age = Column(Integer)
    favorites = relationship(Favorites)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
