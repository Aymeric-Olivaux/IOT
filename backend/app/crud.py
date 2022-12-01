from sqlalchemy.orm import Session

from . import models, schemas

import datetime

def get_user(db: Session, email: str, password: str):
    return db.query(models.User).filter(models.User.email == email, models.User.password == password).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def insert_data(db: Session, data: schemas.DataCreate):
    db_data = models.Data(device_id = data.device_id, collected_at=datetime.datetime.now(), decibels = data.decibels)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def fetch_data_minute(db: Session, device_id: int):
    last_minute = datetime.datetime.now() - datetime.timedelta(minutes=1)
    return db.query(models.Data).filter(models.Data.device_id == device_id, models.Data.collected_at >= last_minute).all()

def fetch_data_hour(db: Session, device_id: int):
    last_hour = datetime.datetime.now() - datetime.timedelta(hours=1)
    return db.query(models.Data).filter(models.Data.device_id == device_id, models.Data.collected_at >= last_hour).all()