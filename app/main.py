from fastapi import FastAPI
from sqlalchemy.ext.declarative import declarative_base

from models import Contact
from database import SessionLocal, engine
from crud import create_contact, read_contacts, read_contact, update_contact, delete_contact, upcoming_birthdays

app = FastAPI()

Base = declarative_base()
Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)