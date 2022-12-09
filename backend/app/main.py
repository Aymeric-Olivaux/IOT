from typing import Union

from fastapi import Depends, FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from . import models, schemas
from .crud import get_user, get_user_by_email, create_user, insert_data, fetch_data_minute, fetch_data_hour, fetch_data_day, fetch_data_week, fetch_data_month
from datetime import datetime
import logging

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    )

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/login", response_model=schemas.User)
def login(user: schemas.User, db: Session = Depends(get_db)):
    db_user = get_user(db, user.email, user.password)
    if (db_user == None):
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.post("/register", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)
    if (db_user != None):
        raise HTTPException(status_code=400, detail="User already exists")
    return create_user(db=db, user=user)

@app.post("/data", response_model=schemas.Data)
def post_data(data: schemas.DataCreate, db: Session = Depends(get_db)):
    db_data = insert_data(db, data)
    return db_data

@app.get("/data/{device_id}/minute")
def get_data_minute(device_id: int, db: Session = Depends(get_db)):
    data =  fetch_data_minute(db, device_id)
    decibels_data = []
    time_data = []
    for d in data:
        decibels_data.append(d.decibels)
        t = d.collected_at
        time_data.append(t.strftime("%H:%M:%S"))

    return {"decibels": decibels_data, "time": time_data}

@app.get("/data/{device_id}/hour")
def get_data_hour(device_id: int, db: Session = Depends(get_db)):
    data =  fetch_data_hour(db, device_id)
    decibels_data = []
    time_data = []
    prev = 0
    length = len(data)

    # print all data timestamps
    for d in data:
        print(d.collected_at)
    
    # Average the data for an interval of 5 minutes for the last hour
    for i in range(0, length, length // 12):
        avg = 0
        for j in range(prev, i):
            avg += data[j].decibels
        if (i - prev == 0):
            avg = data[i].decibels
        else:
            avg /= (i - prev)
        decibels_data.append(avg)
        t = data[i].collected_at
        time_data.append(t.strftime("%H:%M"))
        prev = i
    return {"decibels": decibels_data, "time": time_data}

@app.get("/data/{device_id}/day")
def get_data_day(device_id: int, db: Session = Depends(get_db)):
    data =  fetch_data_day(db, device_id)
    decibels_data = []
    time_data = []
    prev = 0
    length = len(data)
    
    # Average the data for every hour for the last day
    for i in range(0, length, length // 24):
        avg = 0
        for j in range(prev, i):
            avg += data[j].decibels
        if (i - prev == 0):
            avg = data[i].decibels
        else:
            avg /= (i - prev)
        decibels_data.append(avg)
        t = data[i].collected_at
        time_data.append(t.strftime("%H:%M"))
        prev = i
    return {"decibels": decibels_data, "time": time_data}

@app.get("/data/{device_id}/week")
def get_data_week(device_id: int, db: Session = Depends(get_db)):
    data =  fetch_data_week(db, device_id)
    decibels_data = []
    time_data = []
    prev = 0
    length = len(data)
    
    # Average the data with 2 points for every day for the last week
    for i in range(0, length, length // 14):
        avg = 0
        for j in range(prev, i):
            avg += data[j].decibels
        if (i - prev == 0):
            avg = data[i].decibels
        else:
            avg /= (i - prev)
        decibels_data.append(avg)
        t = data[i].collected_at
        # format the date to monday hour, tuesday hour, etc.
        time_data.append(t.strftime("%a %H:%M"))
        prev = i
    return {"decibels": decibels_data, "time": time_data}

@app.get("/data/{device_id}/month")
def get_data_month(device_id: int, db: Session = Depends(get_db)):
    data =  fetch_data_month(db, device_id)
    decibels_data = []
    time_data = []
    prev = 0
    length = len(data)
    
    # Average the data for every day for the last month
    for i in range(0, length, length // 30):
        avg = 0
        for j in range(prev, i):
            avg += data[j].decibels
        if (i - prev == 0):
            avg = data[i].decibels
        else:
            avg /= (i - prev)
        decibels_data.append(avg)
        t = data[i].collected_at
        time_data.append(t.strftime("%D"))
        prev = i
    return {"decibels": decibels_data, "time": time_data}