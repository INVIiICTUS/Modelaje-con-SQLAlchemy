import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class user(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)

class favoritos(Base):
    __tablename__ = 'favoritos'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    items = Column(Integer, ForeignKey('user.id'))
    def to_dict(self):
        return {}
    

class vehículos(Base):
    __tablename__ = 'Vehiculos'
    id = Column(Integer, primary_key=True)
    velocidad = Column(String(250), nullable=False)
    combustible = Column(String(250), nullable=False)
    capacidad = Column(Integer, ForeignKey('personajes.id'))


class personajes(Base):
    __tablename__ = 'personajes'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(250), nullable=False)
    altura = Column(Integer, ForeignKey('personajes.id'))
    def to_dict(self):
        return {}


class planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    poblacion = Column(String(250), nullable=False)
    galaxia = Column(Integer, ForeignKey('personajes.id'))
    def to_dict(self):
        return {}


render_er(Base, 'diagram.png')