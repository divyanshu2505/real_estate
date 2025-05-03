from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Property(Base):
    __tablename__ = 'properties'
    id = Column(Integer, primary_key=True, index= True)
    title = Column(String, index= True)
    description = Column(String)
    price = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

    