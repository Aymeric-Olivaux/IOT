from typing import Union

from fastapi import Depends, FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from . import models, schemas
from .crud import get_user, get_user_by_email, create_user, insert_data, fetch_data_minute, fetch_data_hour
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
def get_data_minute(device_id: int, db: Session = Depends(get_db)):
    data =  fetch_data_hour(db, device_id)
    decibels_data = []
    time_data = []
    prev = 0
    length = len(data)
    for i in range(50, length, 50):
        decibels_data.append(sum(d.decibels for d in data[prev:i])/50)
        t = data[prev + 25].collected_at
        time_data.append(t.strftime("%H:%M"))
        prev = i
    return {"decibels": decibels_data, "time": time_data}