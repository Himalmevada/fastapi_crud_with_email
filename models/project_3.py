from sqlalchemy import Column, Integer, String, Date
from config.db import Base

class Project3User(Base):
    __tablename__ = 'prj_3_user'
    id = Column(Integer, primary_key=True, index=True)
    mobile_number = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    dob = Column(Date)