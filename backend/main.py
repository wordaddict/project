from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import models, schemas, crud
from backend.database import SessionLocal, engine, Base
from backend.utils import hash_password, verify_password  # Make sure utils.py has these
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from backend.utils import create_access_token
from datetime import timedelta
from backend.utils import get_current_user


Base.metadata.create_all(bind=engine)
app = FastAPI()

# Allow requests from your frontend domain
origins = [
    "https://wordaddict.github.io/project",  # Your Render frontend URL
    "http://localhost:8000",                       
    "http://127.0.0.1:8000",
    "http://localhost:5500",                       
    "http://127.0.0.1:5500"                               
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@app.get("/")
def read_root():
    return {"message": "Homeless Shelter Management API is running."}

# Signup route
@app.post("/signup", response_model=schemas.User)
def signup(user: schemas.UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(models.ShelterUser).filter(models.ShelterUser.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    hashed_pw = hash_password(user.password)
    new_user = models.ShelterUser(
        name=user.name,
        username=user.username,
        hashed_password=hashed_pw,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login")
def login(user: schemas.LoginSchema, db: Session = Depends(get_db)):
    db_user = db.query(models.ShelterUser).filter(models.ShelterUser.username == user.username).first()
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    access_token = create_access_token(data={"sub": db_user.username})

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "username": db_user.username,
        "name": db_user.name,
        "role": db_user.role
    }

@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.get("/assistances/", response_model=List[schemas.Assistance])
def get_assistances(db: Session = Depends(get_db), current_user: models.ShelterUser = Depends(get_current_user)):
    return db.query(models.AssistanceRecord).filter(models.AssistanceRecord.user_id == current_user.id).all()

@app.get("/donations/", response_model=List[schemas.Donation])
def get_donations(
    db: Session = Depends(get_db),
):
    return db.query(models.Donation).all()

@app.post("/donations/", response_model=schemas.Donation)
def add_donation(
    donation: schemas.DonationCreate,
    db: Session = Depends(get_db),
    current_user: models.ShelterUser = Depends(get_current_user)
):
    return crud.add_donation(db, donation, donor_name=current_user.name)

# 🔸 New GET for shifts
@app.get("/shifts/", response_model=List[schemas.Shift])
def get_shifts(db: Session = Depends(get_db)):
    return db.query(models.VolunteerShift).all()

@app.post("/shifts/", response_model=schemas.Shift)
def add_shift(
    shift: schemas.ShiftCreate, 
    db: Session = Depends(get_db),
    current_user: models.ShelterUser = Depends(get_current_user)
):
    db_shift = models.VolunteerShift(
        volunteer_id=current_user.id,  # Use ID from token here
        shift_time=shift.shift_time
    )
    db.add(db_shift)
    db.commit()
    db.refresh(db_shift)
    return db_shift


@app.post("/assistances/", response_model=schemas.Assistance)
def add_assistance(record: schemas.AssistanceCreate, db: Session = Depends(get_db), current_user: models.ShelterUser = Depends(get_current_user)):
    print(f"Logged in as: {current_user.username}, ID: {current_user.id}")

    # Use current_user.id from the token, not from the frontend
    db_record = models.AssistanceRecord(
        user_id=current_user.id,
        service=record.service,
        notes=record.notes,
        timestamp=record.timestamp
    )
    db.add(db_record)
    db.commit()
    db.refresh(db_record)
    return db_record

# 🔹 New GET for donations
@app.get("/donations/", response_model=List[schemas.Donation])
def get_donations(db: Session = Depends(get_db)):
    return db.query(models.Donation).all()


