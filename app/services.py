
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
  
  query_filter = {"name": user.name}
  if DB_CONNECT.count(query_filter) > 0:
      return None, Error("name already in use", 400)
  
  account = Person(
     id = ObjectId(),
     name=user.name,
     email= user.email,

  )

  try:
      DB_CONNECT.create(account)
  except Exception as e:
      print(e)
      return None, Error("failed to create account", 500)

  return account, None

# function to get all persons
def get_all_users():

  accounts = DB_CONNECT.fetch_all()
  
  return accounts, None

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
    email: str = None,
    user_object: Person = None,

):
  
  if name is not None:
    # check if name is already in use

    account, error = get_single_user(name)

    if account:
       return None, Error("name already in use", 400)
    user_object.name = name

  if email is not None:

    if is_valid_email(email) == False:
       return None, Error("invalid email", 400)
    
    user_object.email = email
  user_object.updated_at = datetime.now()

  try:
      DB_CONNECT.update({"_id": user_object.id}, user_object.to_dict())
      return user_object, None
  except Exception:
      return None, Error("failed to update user", 500)
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