from typing import Any

from fastapi import APIRouter, Depends, HTTPException

from app import crud

router = APIRouter()

@router.get("/")
def get_block_latest() -> Any:
    """
    Get latest block
    """
    block = crud.block.get_latest_block()
    if not block:
        raise HTTPException(status_code=404, detail="Block not found")
    return block


@router.get("/height/{height}")
def get_block_by_height(
    *,
    height: int,
) -> Any:
    """
    Get block by height.
    """
    block = crud.block.get_by_height(height)
    if not block:
        raise HTTPException(status_code=404, detail="Block not found")
    return block

@router.get("/hash/{hash}")
def get_block_by_hash(
    *,
    hash: str,
) -> Any:
    """
    Get block by hash.
    """
    block = crud.block.get_by_hash(hash)
    if not block:
        raise HTTPException(status_code=404, detail="Block not found")
    return block
