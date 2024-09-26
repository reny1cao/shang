from pydantic import BaseModel
from typing import List

class StockSummary(BaseModel):
    symbol: str
    price: float
    change_percent: float

class MarketSummary(BaseModel):
    index_value: float
    index_change: float
    top_gainers: List[StockSummary]
    top_losers: List[StockSummary]
    market_sentiment: str