from sqlalchemy import Column, Integer, String
from config.db import Base

class Project2User(Base):
    __tablename__ = 'prj_2_user'
    id = Column(Integer, primary_key=True, index=True)
    mobile_number = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    hashtag = Column(String)