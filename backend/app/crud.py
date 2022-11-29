from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, email: str, password: str):
    return db.query(models.User).filter(models.User.email == email, models.User.password == password).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    password = user.password
    db_user = models.User(email=user.email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user