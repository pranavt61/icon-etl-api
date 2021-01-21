from fastapi import APIRouter

from app.api.api_v1.endpoints import items, login, users, utils, blocks, transactions, events

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
api_router.include_router(items.router, prefix="/items", tags=["items"])
api_router.include_router(blocks.router, prefix="/blocks", tags=["blocks"])
api_router.include_router(transactions.router, prefix="/tx", tags=["transactions"])
api_router.include_router(events.router, prefix="/events", tags=["contract events"])
