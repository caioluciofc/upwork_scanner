from pydantic import BaseModel


class Address(BaseModel):
    line1: str
    line2: str
    city: str
    state: str
    postal_code: str
    country: str


class UpworkUser(BaseModel):
    user_rid: str
    last_name: str
    full_name: str
    phone_number: str
    id_verified: bool
    email: str
    email_verified: bool
    profile_pic_link: str
    address: Address
