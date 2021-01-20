from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException

from app import crud

router = APIRouter()

@router.get("/height/{height}")
def read_blocks_by_height(
    *,
    height: int,
) -> Any:
    """
    Get block by height.
    """
    blocks = crud.block.read_by_height(height)
    if not blocks:
        raise HTTPException(status_code=404, detail="Block not found")
    return blocks

@router.get("/hash/{hash}")
def read_block_by_hash(
    *,
    hash: str,
) -> Any:
    """
    Get block by height.
    """
    block = crud.block.read_by_hash(hash)
    if not block:
        raise HTTPException(status_code=404, detail="Block not found")
    return block

@router.get("/tx_count/{count}")
def read_block_by_hash(
    *,
    count: int,
) -> Any:
    """
    Get block by height.
    """
    blocks = crud.block.read_by_tx_count(count)
    if not blocks:
        raise HTTPException(status_code=404, detail="Block not found")
    return blocks

@router.get("/min_tx_count/{count}")
def read_block_by_hash(
    *,
    count: int,
) -> Any:
    """
    Get block by height.
    """
    blocks = crud.block.read_by_min_tx_count(count)
    if not blocks:
        raise HTTPException(status_code=404, detail="Block not found")
    return blocks

@router.get("/max_tx_count/{count}")
def read_block_by_hash(
    *,
    count: int,
) -> Any:
    """
    Get block by height.
    """
    blocks = crud.block.read_by_max_tx_count(count)
    if not blocks:
        raise HTTPException(status_code=404, detail="Block not found")
    return blocks
