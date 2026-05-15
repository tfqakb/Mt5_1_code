import MetaTrader5 as mt5
from crewai.tools import BaseTool
import pandas as pd
import ta
import json

class IndicatorTool(BaseTool):

    name: str = "Indicator Tool"
    description: str = "A tool to calculate EMA and RSI indicators for a given symbol and timeframe."

    def _run(self, market_json: str):
        df = pd.read_json(market_json)
        df["RSI"] = ta.momentum.RSIIndicator(df["close"]).rsi()
        df["EMA_20"] = ta.trend.EMIndicator(df["close"], window=20).ema_indicator()

        return json.dumps({"rsi": float(df["RSI"].iloc[-1]), 
                           "ema_20": float(df["EMA_20"].iloc[-1])})