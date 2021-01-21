from fastapi import APIRouter

from app.api.api_v1.endpoints import blocks, transactions, events

api_router = APIRouter()
api_router.include_router(blocks.router, prefix="/blocks", tags=["blocks"])
api_router.include_router(transactions.router, prefix="/tx", tags=["transactions"])
api_router.include_router(events.router, prefix="/events", tags=["contract events"])
