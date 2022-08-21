from services.mongo_db import MongoDbClient

def test_mongo_connection():
    my_mongo = MongoDbClient()
    assert my_mongo.client
    assert my_mongo.db is not None
