from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from app import crud

router = APIRouter()

@router.get("/hash/{hash}")
def get_tx_by_hash(
        *,
        hash: str
) -> Any:
    """
    Get transaction by hash
    """
    tx = crud.transaction.get_by_hash(hash)
    if not tx:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return tx

@router.get("/block")
def get_txs_latest_block() -> Any:
    """
    Get transactions in latest block
    """
    txs = crud.transaction.get_by_latest_block()
    if len(txs) == 0:
        raise HTTPException(status_code=404, detail="Transactions not found")
    return txs

@router.get("/block/{height}")
def get_txs_by_height(
        *,
        height: int
) -> Any:
    """
    Get transactions by block height
    """
    txs = crud.transaction.get_by_block(height)
    if len(txs) == 0:
        raise HTTPException(status_code=404, detail="Transactions not found")
    return txs
