import os
from pymongo.mongo_client import MongoClient

username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")

uri = f"mongodb+srv://{username}:{password}@wedding-cluster.sqkmc.mongodb.net/?retryWrites=true&w=majority&appName=wedding-cluster"

client = MongoClient(uri)


def get_gifts():
    collection = client["wedding"]["jjgifts"]
    return collection.find()

def update_gift(state_key, status: bool):
    collection = client["wedding"]["jjgifts"]

    collection.update_one(
        {"uuid": state_key},  # Filter
        {"$set": {"reserved": status}}  # Update operation
    )
