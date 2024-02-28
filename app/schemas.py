from pydantic import BaseModel
from datetime import date

class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date
    additional_data: str = None

class ContactUpdate(ContactCreate):
    pass

class ContactResponse(ContactCreate):
    id: int
