from typing import List
from fastapi import Depends, FastAPI, HTTPException
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session

import crud, models, schemas
from database import SessionLocal, engine

# creates database tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# create a dependency to make a new session per request and close it after the request is completed
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")
def main():
    ''' default function to fetch the backend documentation using starlette redirect response'''
    return RedirectResponse(url="/docs/")


@app.post("/customers/", response_model=schemas.Customer)
def reserve_room(customer: schemas.Customer, db: Session = Depends(get_db)):
    ''' make a function call to reserve room''' 
    return crud.reserve_room(db=db, customer=customer)


@app.get("/customer/{customer_id}", response_model=schemas.Customer)
def get_customer_by_id(customer_id: int, db: Session = Depends(get_db)):
    ''' fetch the customer by customer id if user is not in the system returns user not found'''
    db_customer = crud.get_customer_by_id(db, customer_id=customer_id)
    if db_customer is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_customer


@app.get("/rooms/", response_model=List[schemas.Room])
def  get_rooms(db: Session = Depends(get_db)):
    ''' fetch rooms from db which is created by the admin for the customer to reserve'''
    rooms = crud.get_rooms(db)
    return rooms

@app.get("/room/{room_id}", response_model=schemas.Room)
def get_room_by_id(room_id: int, db: Session = Depends(get_db)):
    '''fetch room by id to get more details about it separately'''
    db_room = crud.get_room_by_room_no(db, room_id=room_id)
    if db_room is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return db_room

@app.put("/pay_amount/",response_model=schemas.Customer)
def pay_amount_to_book_rooms(customer_id:int,account_no:int,mpin:int,db:Session=Depends(get_db)):
    '''make payment to book the room once it is selected in reserve_room function'''
    pay=crud.pay_amount(customer_id,account_no,mpin,db=db)
    return pay

@app.delete("/customer/{customer_id}/")
def cancel_room(customer_id:int,db: Session = Depends(get_db)):
    '''cancels the booking if customer dont want that room or need to reserve again '''
     db_customer = crud.get_customer_by_id(db, customer_id=customer_id)
     return crud.cancel_room(db,db_customer)

    
      

