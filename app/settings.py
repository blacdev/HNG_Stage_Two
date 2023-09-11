from decouple import config


DATABASE_URI = config("DATABASE_URI")
DATABASE_NAME = config("DATABASE_NAME")
COLLECTION_NAME = config("COLLECTION_NAME")
EMAIL_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
