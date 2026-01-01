from sqlalchemy import Column, String, Integer
from db import Base


class User(Base):
    __tablename__ = 'usersinfo'
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    otp = Column(Integer, index=True)
