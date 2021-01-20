from odmantic import Model

class Block(Model):
    signature: str
    item_id: str
    next_leader: str
    transaction_count: int
    type: str
    version: str
    peer_id: str
    number: int
    merkle_root_hash: str
    item_timestamps: str
    hash: str
    parent_hash: str
    timestamps: int

    class Config:
        collection = "blocks"