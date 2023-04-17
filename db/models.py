from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

import datetime


class Kasa(Base):
    __tablename__ = "kasa"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32), index=True, unique=True)
    is_valid = Column(Boolean, default=True)


class Obj(Base):
    __tablename__ = "obj"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32), unique=True)
    is_valid = Column(Boolean, default=True)


class Clients(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32), unique=True)
    is_valid = Column(Boolean, default=True)
    types_info = relationship("Types", back_populates="types_info")


class Types(Base):
    __tablename__ = "types"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(32), unique=True)
    with_contragent = Column(Boolean, default=False)
    is_valid = Column(Boolean, default=True)


class Action(Base):
    __tablename__ = "action"
    id = Column(Integer, primary_key=True, index=True)
    action_data = Column(DateTime, default=datetime.datetime.now())
    kasa_id = Column(Integer, ForeignKey(Kasa.id, ondelete="CASCADE"))
    types = Column(Integer, ForeignKey(Types.id, ondelete="CASCADE"))
    contragents = Column(
        Integer, ForeignKey(Clients.id, ondelete="CASCADE"), nullable=True
    )
    kasa_to_id = Column(Integer, ForeignKey(Kasa.id, ondelete="CASCADE"), nullable=True)
    amount = Column(Integer)
    comments = Column(String, nullable=True)
