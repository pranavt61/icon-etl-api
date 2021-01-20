from app.db.session import MongoClient

from app.db.aio_engine import MongoEngine
from app.models import Block

class CRUDBlock():
    def read_by_height(self, height):
        block_cursor = MongoClient["icon"]["blocks"].find({ "number": { "$eq": height } }, { '_id': 0 })

        blocks = []
        for b in block_cursor:
            blocks.append(b)

        return blocks

    def read_by_hash(self, hash):
        block = MongoClient["icon"]["blocks"].find_one({ "hash": { "$eq": hash } }, { '_id': 0 })

        return block

    def read_by_tx_count(self, count):
        block_cursor = MongoClient["icon"]["blocks"].find({ "transaction_count": { "$eq": count } }, { '_id': 0 })

        blocks = []
        for b in block_cursor:
            blocks.append(b)

        return blocks

    def read_by_min_tx_count(self, count):
        block_cursor = MongoClient["icon"]["blocks"].find({ "transaction_count": { "$gte": count } }, { '_id': 0 })

        blocks = []
        for b in block_cursor:
            blocks.append(b)

        return blocks

    def read_by_max_tx_count(self, count):
        block_cursor = MongoClient["icon"]["blocks"].find({ "transaction_count": { "$lte": count } }, { '_id': 0 })

        blocks = []
        for b in block_cursor:
            blocks.append(b)

        return blocks

'''
class CRUDBlock_MONG():
    async def read_by_height(self, height):
        block = await MongoEngine.find(Block, Block.number == height)

        return block

block_mongo = CRUDBlock_MONG()
'''
block = CRUDBlock()
