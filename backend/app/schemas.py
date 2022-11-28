from pydantic import BaseModel
import datetime

class UserBase(BaseModel):
    email: str
    password: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    email: str
    password: str

    class Config:
        orm_mode = True

class DeviceBase(BaseModel):
    owner_id: int

class DeviceCreate(DeviceBase):
    pass

class Device(DeviceBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class DataBase(BaseModel):
    device_id: int
    collected_at: datetime.datetime
    decibels: int

class DataCreate(DataBase):
    pass

class Data(DataBase):
    id: int
    device_id: int
    collected_at: datetime.datetime
    decibels: int

    class Config:
        orm_mode = True