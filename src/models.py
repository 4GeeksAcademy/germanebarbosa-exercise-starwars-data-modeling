import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Planet(Base):
    __tablename__ = 'planet'

    id = Column(Integer, primary_key=True, nullable=True)
    planet_name = Column(String(250), nullable=True)
    population = Column(String(250))

class Character(Base):
    __tablename__ = 'character'

    id = Column(Integer, primary_key=True, nullable=True)
    character_name = Column(String(250), nullable=True)
    age = Column(Integer)

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=True)
    user_name = Column(String(250), nullable=True)
    password = Column(String(250))

class Favorite(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
