from typing import Union

from fastapi import Depends, FastAPI, Body, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from . import models, schemas
from .crud import get_user, get_user_by_email, create_user, insert_data

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
