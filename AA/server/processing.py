from pymongo import MongoClient
import hashlib
import os

client = MongoClient('mongodb://localhost:27017/')
db = client['healthcare']
users_collection = db['users']
def create_sample_users():
    if users_collection.count_documents({}) == 0:
        sample_users = [
            {
                "username": "admin",
                "password": "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f",
                "ID": "1",
                "attribute": ["admin"]
            }
        ]
        users_collection.insert_many(sample_users)
        print("Sample users created.")
    else:
        print("Users already exist.")

def authenticate_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    user = users_collection.find_one({"username": username, "password": hashed_password})
    return user