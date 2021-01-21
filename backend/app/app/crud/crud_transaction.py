from app.db.session import MongoClient

from app.db.aio_engine import MongoEngine
from app.models import Block

class CRUDTransaction():
    def get_by_hash(self, hash):
        tx = MongoClient["icon"]["transactions"]\
            .find_one({ "hash": { "$eq": hash } }, { "_id": 0 })

        return tx

    def get_by_latest_block(self):
        latest_block_height = MongoClient["icon"]["blocks"]\
            .find_one({}, { "_id": 0, "number": 1 }, sort=[("number", -1)])["number"]

        tx_cursor = MongoClient["icon"]["transactions"] \
            .find({"block_number": {"$eq": latest_block_height}}, {"_id": 0})

        txs = []
        for t in tx_cursor:
            txs.append(t)

        return txs

    def get_by_block(self, height):
        tx_cursor = MongoClient["icon"]["transactions"]\
            .find({ "block_number": { "$eq": height } }, { "_id": 0 })

        txs = []
        for t in tx_cursor:
            txs.append(t)

        return txs

transaction = CRUDTransaction()
