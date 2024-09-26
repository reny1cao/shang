from fastapi import APIRouter
from app.api.routes import market_summary

router = APIRouter()

router.include_router(market_summary.router, prefix="/api/market-summary", tags=["market"])