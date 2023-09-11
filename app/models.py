from bson.objectid import ObjectId
from datetime import datetime


class Person:
  def __init__(
      self,
      id: ObjectId,
      name: str,
      age: int,
      phone_number: str,
      email: str,
      address: str,
      city: str,
      state: str,
      country: str
  ):
    self.id = id
    self.name = name
    self.age = age
    self.phone_number = phone_number
    self.email = email
    self.address = address
    self.city = city
    self.state = state
    self.country = country
    self.created_at = datetime.now()
    self.updated_at = datetime.now()

    # don't write these fields to the database
    self.used_projection = False

  def to_dict(self):
    data = {
        "_id": self.id,
        "name": self.name,
        "age": self.age,
        "phone_number": self.phone_number,
        "email": self.email,
        "address": self.address,
        "city": self.city,
        "state": self.state,
        "country": self.country,
        "created_at": self.created_at,
        "updated_at": self.updated_at

    }
    return data