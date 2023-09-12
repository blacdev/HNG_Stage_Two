from pydantic import BaseModel, validator
from app.models import Person
from fastapi import HTTPException

class User_schema(BaseModel):
    name: str

    # handle age validation
  

class User_Create_response(BaseModel):
    id: str
    name: str

class User_response(User_schema):
    id: str

class User_update_schema(User_schema):
    pass
def user_response_serializer(account: Person):
    """account_response_serializer serializes an account to an AccountResponse"""
    
    return User_response(
        id=str(account.id),
        name=account.name,
    )


def usercreate_response_serializer(account: Person):
    """account_response_serializer serializes an account to an AccountResponse"""

    return User_Create_response(
        id=str(account.id),
        name=account.name,
    )