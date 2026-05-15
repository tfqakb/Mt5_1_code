from crewai.tools import BaseTool
import MetaTrader5 as mt5
import pandas as pd

class MarketDataTool(BaseTool):
    name: str = "Market Data Tool"
    description: str = "A tool to fetch forex market OHLCV data using MetaTrader 5."

    def _run(self, symbol:str):
        mt5.initialize()

        rates = mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_M5, 0, 200)
        mt5.shutdown()

        df = pd.DataFrame(rates)

        return df.to_json()
