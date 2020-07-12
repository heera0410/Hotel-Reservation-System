#import the sqlalchemy libraries
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# create a database url for sqlalchemy and the file reservation.db must be in the same directory or change the url accordingly for the sqlite database to connect
SQLALCHEMY_DATABASE_URL = "sqlite:///./reservation.db"

# create a engine and set check_same_thread to false only for sqlite to check whether it has unique database session for different request
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# create a sessionlocal object to create database session using session maker function
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This function returns a class which is inherited to create database classes or models -->The Object Relationship Model in models.py
Base = declarative_base()
