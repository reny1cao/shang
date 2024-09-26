from fastapi import APIRouter
from app.schemas.market_summary import MarketSummary
from app.services.market_analysis import generate_market_summary

router = APIRouter()

@router.get("/", response_model=MarketSummary)
async def get_market_summary():
    return generate_market_summary()