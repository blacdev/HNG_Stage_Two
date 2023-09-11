from pydantic import BaseModel, validator
from app.models import Person
from fastapi import HTTPException

class User_schema(BaseModel):
    name: str
    age: int
    phone_number: str
    email: str
    address: str
    city: str
    state: str
    country: str

    # handle age validation
    
    @validator("age", pre=True, always=True)
    def age_(cls, age):
        if isinstance(age, int) is False:
            raise HTTPException(status_code=400, detail="age must be an integer")
        return age
    

class User_Create_response(BaseModel):
    id: str
    name: str
    email: str

class User_response(User_schema):
    id: str

class User_update_schema(User_schema):
    pass
def user_response_serializer(account: Person):
    """account_response_serializer serializes an account to an AccountResponse"""
    
    return User_response(
        id=str(account.id),
        name=account.name,
        email=account.email,
        age=account.age,
        phone_number=account.phone_number,
        address=account.address,
        city=account.city,
        state=account.state,
        country=account.country,
        created_at=account.created_at,
        updated_at=account.updated_at
    )


def usercreate_response_serializer(account: Person):
    """account_response_serializer serializes an account to an AccountResponse"""

    return User_Create_response(
        id=str(account.id),
        email=account.email,
        name=account.name,
    )