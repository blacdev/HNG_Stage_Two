from bson.objectid import ObjectId
from datetime import datetime


class Person:
  def __init__(
      self,
      id: ObjectId,
      name: str

  ):
    self.id = id
    self.name = name
    self.created_at = datetime.now()
    self.updated_at = datetime.now()

    # don't write these fields to the database
    self.used_projection = False

  def to_dict(self):
    data = {
        "_id": self.id,
        "name": self.name,
        "created_at": self.created_at,
        "updated_at": self.updated_at

    }
    return data