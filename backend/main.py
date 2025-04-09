from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend import models, schemas, crud
from database import SessionLocal, engine, Base

Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@app.get("/")
def read_root():
    return {"message": "Homeless Shelter Management API is running."}


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@app.post("/assistances/", response_model=schemas.Assistance)
def add_assistance(record: schemas.AssistanceCreate, db: Session = Depends(get_db)):
    return crud.add_assistance(db, record)

@app.post("/donations/", response_model=schemas.Donation)
def add_donation(donation: schemas.DonationCreate, db: Session = Depends(get_db)):
    return crud.add_donation(db, donation)

@app.post("/shifts/", response_model=schemas.Shift)
def add_shift(shift: schemas.ShiftCreate, db: Session = Depends(get_db)):
    return crud.add_shift(db, shift)
