from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException

from app import crud

router = APIRouter()

@router.get("/tx/{tx_hash}")
def get_events_by_hash(
        *,
        tx_hash: str
) -> Any:
    """
    Get event by transaction
    """
    events = crud.event.get_by_tx(tx_hash)
    if len(events) == 0:
        raise HTTPException(status_code=404, detail="Events not found")
    return events

@router.get("/block")
def get_txs_latest_block() -> Any:
    """
    Get events in latest block
    """
    events = crud.event.get_by_latest_block()
    if len(events) == 0:
        raise HTTPException(status_code=404, detail="Events not found")
    return events

@router.get("/block/{height}")
def get_txs_by_height(
        *,
        height: int
) -> Any:
    """
    Get events by block height
    """
    events = crud.event.get_by_block(height)
    if len(events) == 0:
        raise HTTPException(status_code=404, detail="Events not found")
    return events
