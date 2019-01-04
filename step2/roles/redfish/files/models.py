#!/usr/bin/python3
# -*- coding: utf-8 -*-
# __author__ = 'Benjamin'

from sqlalchemy import Column, String, Integer, func
from sqlalchemy.types import DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Entries(Base):
    __tablename__ = 'last_entries'
    id = Column(Integer, primary_key=True)
    ip = Column(String)
    name = Column(String)
    time = Column(DateTime(timezone=True), default=func.now())
    sqlite_autoincrement = True