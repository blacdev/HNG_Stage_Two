
from app.models import Person
from pymongo import MongoClient


from app.settings import DATABASE_NAME, DATABASE_URI, COLLECTION_NAME

client = MongoClient(host=DATABASE_URI)


class Database:
    def __init__(self, COLLECTION_NAME):
        self.database = client[DATABASE_NAME]
        self.collection = self.database[COLLECTION_NAME]

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
    def create(self, data):
        self.collection.insert_one(data.to_dict())

    def find_one(self, query_filter):
        data = self.collection.find_one(query_filter)
        
        if data is not None:
            return Person(
                id = data.get("_id", ),
                name= data.get("name"),
                age = data.get("age"),
                phone_number=data.get("phone_number"),
                email=data.get("email"),
                address= data.get("address"),
                city= data.get("city"),
                state= data.get("state"),
                country= data.get("country"),
            )
        return None


    def count(self, query_filter):
        return self.collection.count_documents(query_filter)


    def update(self, query_filter, obj):
        self.collection.find_one_and_replace(query_filter, obj)
    
    def delete(self, query_filter):
        result = self.collection.delete_one(query_filter)
        return result.deleted_count > 0


DB_CONNECT = Database(COLLECTION_NAME)