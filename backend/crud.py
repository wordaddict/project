from sqlalchemy.orm import Session
from backend import models, schemas


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.ShelterUser(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def add_assistance(db: Session, record: schemas.AssistanceCreate):
    db_record = models.AssistanceRecord(**record.dict())
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

def add_donation(db: Session, donation: schemas.DonationCreate):
    db_donation = models.Donation(**donation.dict())
    db.add(db_donation)
    db.commit()
    db.refresh(db_donation)
    return db_donation

def add_shift(db: Session, shift: schemas.ShiftCreate):
    db_shift = models.VolunteerShift(**shift.dict())
    db.add(db_shift)
    db.commit()
    db.refresh(db_shift)
    return db_shift
