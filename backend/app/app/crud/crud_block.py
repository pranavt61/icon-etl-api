from app.db.session import MongoClient

from app.db.aio_engine import MongoEngine
from app.models import Block

class CRUDBlock():
    def get_latest_block(self):
        block = MongoClient["icon"]["blocks"]\
            .find_one({}, { "_id": 0 }, sort=[("number", -1)])

        return block

    def get_by_height(self, height):
        block = MongoClient["icon"]["blocks"]\
            .find_one({ "number": { "$eq": height } }, { "_id": 0 })

        return block

    def get_by_hash(self, hash):
        block = MongoClient["icon"]["blocks"]\
            .find_one({ "hash": { "$eq": hash } }, { "_id": 0 })

        return block

block = CRUDBlock()
