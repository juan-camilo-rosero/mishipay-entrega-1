from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://mishi:ZMjaQTCsrLC1SeGx@mishipay.dlfmkob.mongodb.net/?retryWrites=true&w=majority&appName=MishiPay"

conn = MongoClient(uri, server_api=ServerApi('1'))
