from sqlalchemy import Column, Integer, String
from database import Base

# base class from database.py is inherited by classes in models.py.The tablename attribute tells the sqlalchemy to refer which table in database
#each attribute is a column in db and it is of type int,string accordingly 
class Customer(Base):
    
    __tablename__ = "Customer"
    customer_id = Column(Integer, primary_key=True,autoincrement=True)
    name= Column(String)
    age= Column(Integer)
    phone_no= Column(Integer)
    email=Column(String,unique=True)
    address=Column(String)
    room_no=Column(Integer)
    status=Column(String)
    date=Column(String)
    length_of_stay=Column(String)    
    account_no=Column(Integer)
    mpin=Column(Integer)

class Room(Base):
    __tablename__ = "Room"

    room_no= Column(Integer, primary_key=True)
    no_of_beds= Column(Integer)
    amount= Column(Integer)



