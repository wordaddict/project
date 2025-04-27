from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    name: str
    username: str
    role: str


class UserCreate(UserBase):
    password: str  # Include password for signup
class User(UserBase):
    id: int
    class Config: orm_mode = True

class LoginSchema(BaseModel):
    username: str
    password: str

class AssistanceBase(BaseModel):
    service: str
    notes: str
    timestamp: datetime

class AssistanceCreate(AssistanceBase): pass
class Assistance(AssistanceBase):
    id: int
    user_id: int   
    class Config: orm_mode = True

class DonationBase(BaseModel):
    item: str
    quantity: int
    timestamp: datetime

class DonationCreate(DonationBase): pass
class Donation(DonationBase):
    id: int
    donor_name: str
    class Config: orm_mode = True

class ShiftBase(BaseModel):
    shift_time: str

class ShiftCreate(ShiftBase): pass
class Shift(ShiftBase):
    id: int
    volunteer_id: int  
    class Config: orm_mode = True
