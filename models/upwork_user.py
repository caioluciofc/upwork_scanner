from pydantic import BaseModel
from typing import

user_object = {
    "first_name": first_name,
    "last_name": last_name,
    "full_name": first_name + " " + last_name,
    "user_rid": user_rid,
    "phone_number": user_phone,
    "id_verified": id_verification,
    "email": email,
    "email_verified": email_verified,
    "profile_pic_link": profile_picture_link,
    "address": {
        "line1": address_line_1,
        "line2": address_line_2,
        "city": city,
        "state": state,
        "postal_code": postal_code,
        "country": country
    }
}

class Address(BaseModel):
    line1: str
    line2: str
    city: str
    state: str
    postal_code: int
    country:str

class UpworkUser(BaseModel):
    user_rid: str
    last_name: str
    full_name: str
    phone_number: str
    id_verified: bool
    email: str
    email_verified: bool
    profile_pic_link: str
    address: