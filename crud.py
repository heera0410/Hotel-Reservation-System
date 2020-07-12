from sqlalchemy.orm import Session
import models, schemas


def get_customer_by_id(db: Session, customer_id: int):
    ''' get the customer details with filter function applied on customer id'''
    return db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()


def get_room_by_room_no(db: Session, room_id:int):
    ''' get the room details with filter function applied on room id'''
    return db.query(models.Room).filter(models.Room.room_no == room_id).first()

def get_rooms(db: Session):
     ''' get all the room details which is in db created by the admin'''
    return db.query(models.Room).all()


def reserve_room(db: Session, customer: schemas.Customer):
    ''' customer id is auto incremented so leaving that all the other required fields is given to reserve a room'''

    db_a = models.Customer(name=customer.name,age=customer.age,phone_no=customer.phone_no,email=customer.email,
    address=customer.address,room_no=customer.room_no,date=customer.date,length_of_stay=customer.length_of_stay)
    db.add(db_a)
    db.commit()
    db.refresh(db_a)
    return db_a

def cancel_room(db: Session, customer: schemas.Customer):
    '''deletes customer details and booked status from db'''
    db.delete(customer)
    db.commit()

def pay_amount(customer_id:int,account_no:int,mpin:int,db:Session):
    '''updates status ,account no,mpin in the db once payment is made'''
    filter_customer=db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()
    setattr(filter_customer,'status','Booked')
    setattr(filter_customer,'account_no',account_no)
    setattr(filter_customer,'mpin',mpin)
    return filter_customer






