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

def fetch_data_day(db: Session, device_id: int):
    last_day = datetime.datetime.now() - datetime.timedelta(days=1)
    return db.query(models.Data).filter(models.Data.device_id == device_id, models.Data.collected_at >= last_day).all()

def fetch_data_week(db: Session, device_id: int):
    last_week = datetime.datetime.now() - datetime.timedelta(weeks=1)
    return db.query(models.Data).filter(models.Data.device_id == device_id, models.Data.collected_at >= last_week).all()

def fetch_data_month(db: Session, device_id: int):
    last_month = datetime.datetime.now() - datetime.timedelta(days=30)
    return db.query(models.Data).filter(models.Data.device_id == device_id, models.Data.collected_at >= last_month).all()

def fetch_threshold(db: Session, device_id: int):
    return db.query(models.Threshold).filter(models.Threshold.device_id == device_id).first()

def update_threshold(db: Session, device_id: int, threshold: schemas.ThresholdCreate):
    db_threshold = fetch_threshold(db, device_id)
    if (db_threshold == None):
        db_threshold = models.Threshold(device_id=device_id, threshold=threshold.threshold)
        db.add(db_threshold)
    else:
        db_threshold.threshold = threshold.threshold
    db.commit()
    db.refresh(db_threshold)
    return db_threshold