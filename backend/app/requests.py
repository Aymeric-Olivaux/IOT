from sqlalchemy.orm import Session

from . import models, schemas

def get_user(db: Session, email: str, password: str):
    return db.query(models.User).filter(models.User.email == email, models.User.password == password).first()

def get_all_users(db: Session):
    return db.query(models.User).all()

