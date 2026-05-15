import MetaTrader5 as mt5
import Config_1 as config
import time
import pandas as pd
import numpy as np

SYMBOL = config.SYMBOL
MAGIC = config.MAGIC
VOLUME = config.VOLUME
ORDERTYPE = config.ORDERTYPE
StOP_LOSS = config.StOP_LOSS
TAKE_PROFIT = config.TAKE_PROFIT
PRICE_DEVIATION = config.PRICE_DEVIATION


    # Connect to MetaTrader 5

mt5.initialize()

def Init():

    if not mt5.initialize():
        print("Initialization() failed")
        return False
        
    if not mt5.symbol_select(SYMBOL, True):
        print("Failed to get symbol")
        return False

    return True

def Loop():
    
    price_info = mt5.symbol_info_tick(SYMBOL)
    if price_info is None:
         print(f"Failed to get price info for {SYMBOL}")
         return True
    
    if ORDERTYPE == mt5.ORDER_TYPE_BUY:
         price = price_info.ask
         stop_loss_price = price_info.bid - StOP_LOSS
         take_profit_price = price_info.bid + TAKE_PROFIT
    else:
         price = price_info.ask
         stop_loss_price = price_info.bid + StOP_LOSS
         take_profit_price = price_info.bid - TAKE_PROFIT

    request = {"action": mt5.TRADE_ACTION_DEAL, "symbol": SYMBOL, "volume": VOLUME, "type": ORDERTYPE,
               "price": price, "sl": stop_loss_price, "tp": take_profit_price, "deviation": PRICE_DEVIATION,
               "type_filling": mt5.ORDER_FILLING_IOC,}
    
    result = mt5.order_send(request)

    if result.retcode != mt5.TRADE_RETCODE_DONE:
         print(f"Order send failed with retcode: {result.retcode}")
         print(result)

    else:
         print("Order succeded")
         print(result)

    return False
    
         
    
def Deinit():
        mt5.shutdown()
        return

if Init():
        while Loop():
            time.sleep(5)
Deinit()
