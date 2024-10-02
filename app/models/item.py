# app/models/item.py
from sqlalchemy import Column, Integer, String
from app.db.database import Base
from pydantic import BaseModel


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
