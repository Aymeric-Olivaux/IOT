from sqlalchemy.orm import Session

from . import models, schemas

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
    db_data = models.Data(device_id = data.device_id, decibels = data.decibels)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data