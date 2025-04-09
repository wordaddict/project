from pydantic import BaseModel
from datetime import datetime

class UserBase(BaseModel):
    name: str
    role: str

class UserCreate(UserBase): pass
class User(UserBase):
    id: int
    class Config: orm_mode = True

class AssistanceBase(BaseModel):
    user_id: int
    service: str
    notes: str
    timestamp: datetime

class AssistanceCreate(AssistanceBase): pass
class Assistance(AssistanceBase):
    id: int
    class Config: orm_mode = True

class DonationBase(BaseModel):
    donor_name: str
    item: str
    quantity: int
    timestamp: datetime

class DonationCreate(DonationBase): pass
class Donation(DonationBase):
    id: int
    class Config: orm_mode = True

class ShiftBase(BaseModel):
    volunteer_id: int
    shift_time: str

class ShiftCreate(ShiftBase): pass
class Shift(ShiftBase):
    id: int
    class Config: orm_mode = True
