# Copyright 2026, MetaQuotes Ltd.
# https://www.mql5.com

from datetime import datetime
import MetaTrader5 as mt5
#import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import time

symbol = "EURUSD"
price_delta = 0.00005


# Connect to MetaTrader 5

mt5.initialize()

if not mt5.initialize():
    print("Initialization() failed")
    mt5.shutdown()
    
if not mt5.symbol_select(symbol, True):
    print("Failed to get symbol")
    mt5.shutdown()

price_info = mt5.symbol_info_tick(symbol)
if not price_info:
    print(f"failed to get price info for {symbol}")
    mt5.shutdown()

starting_price = price_info.bid
price_level_high = starting_price + price_delta
price_level_low = starting_price - price_delta

print(f"Starting price: {starting_price}")
print(f"Price level high: {price_level_high}")
print(f"Price level low: {price_level_low}")

old_price = 0
while True:
    price_info = mt5.symbol_info_tick(symbol)
    if price_info is None:
        continue
    current_price = price_info.bid

    if current_price != old_price:
        print(f"Current price of symbol {symbol} is {current_price}")
        old_price = current_price

    if current_price >= price_level_high:
        print(f"Current price of symbol {symbol} has moved up to {current_price}, above the high level.")
        break
    if current_price <= price_level_low:
        print(f"Current price of symbol {symbol} has moved down to {current_price}, below the low level.")
        break

    time.sleep(5)



# you code here
# 

mt5.shutdown()

