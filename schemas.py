from pydantic import BaseModel
from typing import Optional


class Customer(BaseModel):
    customer_id:int
    name:str
    age:int
    phone_no:int
    email: str
    address:str
    room_no:int
    date:str
    length_of_stay:str
    status:Optional[str]
    account_no:Optional[int]
    mpin:Optional[int]
    class Config:
        '''orm_mode is to get data of type orm model so that it can refer it with dot operator'''
        orm_mode = True


class Room(BaseModel):
    room_no:Optional[int]
    no_of_beds:Optional[int]
    amount:Optional[int]
    class Config:
        orm_mode = True

