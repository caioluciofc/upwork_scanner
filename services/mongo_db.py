from pymongo import MongoClient
import pymongo


class MongoDbClient():
    def __init__(self):
        self.client = MongoClient("mongodb+srv://earthdni:oIB0OdI69touYewU@cluster0.b2o9p.mongodb.net/?retryWrites=true&w=majority")
        self.db = self.client.UpworkScanner

    def write_to_upwork_collection(self, data_model):
        collection = self.db.UpworkUsers
        model_id = collection.insert_one(data_model).inserted_id
        if model_id:
            return model_id
        return False

