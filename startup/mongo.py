# *-* coding: utf-8 *-*
try:
    from pymongo import MongoClient
except ImportError:
    raise ImportError("PyMongo is not installed")


class MongoDB(object):
    def __init__(self, host="localhost", port=27017, database_name=None, collection_name=None):
        try:
            self._connection = MongoClient(host=host, port=port, maxPoolSize=200)
        except Exception as error:
            raise Exception(error)
        self._database = None
        self._collection = None
        if database_name:
            self._database = self._connection[database_name]
        if collection_name:
            self._collection = self._database[collection_name]

    def insert(self, post):
        # add/append/new single record
        post_id = self._collection.insert_one(post).inserted_id
        return post_id

    def get_by_id(self, id):
        # get single record
        ele = self._collection.find_one({"id": id})
        return ele

    def get_all(self):
        # get all records
        eles = self._collection.find({})
        return list(eles)
