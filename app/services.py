
from app.schema import User_schema
from app.models import Person
from app.db import DB_CONNECT
from app.settings import EMAIL_REGEX
import re
from app.Error import Error
from bson.objectid import ObjectId
from bson.errors import InvalidId
from datetime import datetime

# function to create a person
def create_user(user:User_schema):
  if not is_valid_email(user.email):
     return None, Error(msg="Invalid email", code=400)
  
  if isinstance(user.age, int) == False:
      return None, Error(msg="age must be an integer", code=400)
  
  query_filter = {"name": user.name}
  if DB_CONNECT.count(query_filter) > 0:
      return None, Error("name already in use", 400)
  
  account = Person(
     id = ObjectId(),
     name=user.name,
     age = user.age,
     email= user.email,
     phone_number=user.phone_number,
     address=user.address,
     city=user.city,
     state=user.state,
      country=user.country
  )

  try:
      DB_CONNECT.create(account)
  except Exception as e:
      print(e)
      return None, Error("failed to create account", 500)

  return account, None


#  function to get a single person
def get_single_user(idOrName: str):

  """fetch account from database"""
  if idOrName == "":
      return None, Error("id or name is required", 400)
  
  query_filter = {}

  try:
      oid = ObjectId(idOrName)
      query_filter = {"_id": oid}
      
  except InvalidId:
      query_filter["name"] = idOrName

  account = DB_CONNECT.find_one(query_filter)

  if account:
     return account, None
  
  else:
    return  None, Error("user not found", 404)


def update_user( 
    name: str = None,
    age: int = None,
    phone_number: str = None,
    email: str = None,
    address: str = None,
    city: str = None,
    state: str  = None,
    country: str = None,
    user_object: Person = None
):
  
  if name is not None:
    user_object.name = name

  if age is not None:
    user_object.age = age 
  
  if phone_number is not None:
    user_object.phone_number = phone_number

  if email is not None:
    user_object.email = email
  
  if address is not None:
    user_object.address = address
  
  if city is not None:
    user_object.city = city
  
  if state is not None:
    user_object.state = state
  
  if country is not None:
      user_object.country = country

  user_object.updated_at = datetime.now()

  try:
      DB_CONNECT.update({"_id": user_object.id}, user_object.to_dict())
      return user_object, None
  except Exception:
      return None, Error("failed to update transaction", 500)
  pass


def delete_user(account: Person):
  try:
    
    query_filter = {"_id": account.id}
    req = DB_CONNECT.delete(query_filter)

    return req, None
  
  except Exception:
    return None, Error("failed to delete account", 500)
     

def is_valid_email(email):
    if re.fullmatch(EMAIL_REGEX, email):
        return True
    return False