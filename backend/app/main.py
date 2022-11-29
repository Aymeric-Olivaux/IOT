from typing import Union

from fastapi import Depends, FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
from .database import SessionLocal, engine
from sqlalchemy.orm import Session
from . import models, schemas
from .crud import get_user

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
    return db_user