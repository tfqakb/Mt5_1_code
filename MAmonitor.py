# Copyright 2026, MetaQuotes Ltd.
# https://www.mql5.com

from datetime import datetime
import MetaTrader5 as mt5
#import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import time
import pandas as pd

symbol = "EURUSD"

MA_timeframe = mt5.TIMEFRAME_M5
MA_period = 5
MA_price = 'close'

# Connect to MetaTrader 5

mt5.initialize()

def Init():

    if not mt5.initialize():
        print("Initialization() failed")
        return False
        
    if not mt5.symbol_select(symbol, True):
        print("Failed to get symbol")
        return False

    return True

def Loop():
    
    rates = mt5.copy_rates_from_pos(symbol, MA_timeframe, 0, MA_period + 1)
    if rates is None:
            print("No rates data retrieved")
            return True
    
    rates_df = pd.DataFrame(rates)
    rates_df['ma'] = rates_df[MA_price].rolling(window=MA_period).mean()
    ma_value = rates_df['ma'].iloc[-1]

    print(f"Moving average value: {ma_value}")
    
    return True
    
def Deinit():
        mt5.shutdown()
        return

if Init():
        while Loop():
            time.sleep(5)
Deinit()
