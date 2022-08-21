from pydantic import BaseModel
from services.mongo_db import MongoDbClient
from typing import Optional


class Address(BaseModel):
    line1: Optional[str] = "#DataNotFound"
    line2: Optional[str] = "#DataNotFound"
    city: Optional[str] = "#DataNotFound"
    state: Optional[str] = "#DataNotFound"
    postal_code: Optional[str] = "#DataNotFound"
    country: Optional[str] = "#DataNotFound"


class UpworkUser(BaseModel):
    user_rid: str
    last_name: Optional[str] = "#DataNotFound"
    full_name: str
    phone_number: Optional[str] = "#DataNotFound"
    id_verified: bool
    email: str
    email_verified: bool
    profile_pic_link: Optional[str] = "#DataNotFound"
    address: Address
    username: str

    # TODO Query the values before writing, to update the existing model instead of writing a new one
    def write_to_db(self):
        mongo_client = MongoDbClient()
        dict_instance = self.dict()
        dict_instance["_id"] = self.user_rid
        print(dict_instance)
        write_ops = mongo_client.write_to_upwork_collection(self.dict())
        if write_ops:
            return True
        return False