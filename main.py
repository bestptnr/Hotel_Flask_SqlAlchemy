
from requests import session
from sqlalchemy import create_engine,Column,Integer,Float,String,or_,update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///hotel.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
class Room(Base):
    __tablename__= 'room'
    id = Column(Integer,primary_key=True)
    room = Column(String(50))
    price = Column(Float)
Base.metadata.create_all(engine)


room1 = Room(room="Single Room",price=500)
session.add(room1)
session.commit()