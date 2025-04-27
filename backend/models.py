from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from backend.database import Base

class ShelterUser(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String)  # 'staff', 'volunteer', 'donor'

class AssistanceRecord(Base):
    __tablename__ = "assistance"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    service = Column(String)
    notes = Column(String)
    timestamp = Column(DateTime)

class Donation(Base):
    __tablename__ = "donations"
    id = Column(Integer, primary_key=True, index=True)
    donor_name = Column(String)
    item = Column(String)
    quantity = Column(Integer)
    timestamp = Column(DateTime)

class VolunteerShift(Base):
    __tablename__ = "shifts"
    id = Column(Integer, primary_key=True, index=True)
    volunteer_id = Column(Integer, ForeignKey("users.id"))
    shift_time = Column(String)
