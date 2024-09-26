import random
from app.schemas.market_summary import MarketSummary, StockSummary

def get_market_sentiment(index_change: float) -> str:
    if index_change > 1:
        return "Bullish"
    elif index_change < -1:
        return "Bearish"
    else:
        return "Neutral"

def generate_market_summary() -> MarketSummary:
    # This is a mock implementation. In a real-world scenario, 
    # you would fetch this data from a financial API or database.
    index_value = random.uniform(3000, 4000)
    index_change = random.uniform(-2, 2)
    
    def generate_stock_summary():
        return StockSummary(
            symbol=f"STOCK{random.randint(1, 100)}",
            price=random.uniform(10, 1000),
            change_percent=random.uniform(-5, 5)
        )
    
    top_gainers = sorted(
        [generate_stock_summary() for _ in range(5)], 
        key=lambda x: x.change_percent, 
        reverse=True
    )
    
    top_losers = sorted(
        [generate_stock_summary() for _ in range(5)], 
        key=lambda x: x.change_percent
    )
    
    return MarketSummary(
        index_value=index_value,
        index_change=index_change,
        top_gainers=top_gainers,
        top_losers=top_losers,
        market_sentiment=get_market_sentiment(index_change)
    )