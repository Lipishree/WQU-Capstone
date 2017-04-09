"""
@author: lipi
Get all the indicators using talib
Bollinger Bands
ADX
RSI
MACD
SMA
Stochastic 
"""

from STRATEGY_ADX_BB_MACD_RSI import device_strategy
from KEY_PROCESS_INDICATORS import Measure_KPI
import pandas as pd
import talib

def mean_reversion_and_trading_strategy(stock_data):
    # Index data variable
    Index_Close = stock_data['^GSPC'].Close.values
    Index_MA = talib.SMA(stock_data['^GSPC'].Close.values,40)
    #Bollinger bands of 14days SMA
    bands_i = talib.BBANDS(stock_data['^GSPC'].Close.values,40,1.75,1.75)
    Index_BH = bands_i[0]
    Index_BM = bands_i[1]
    Index_BL = bands_i[2]
    Index_ADX = talib.ADX(stock_data['^GSPC'].High.values,\
                          stock_data['^GSPC'].Low.values,\
                          stock_data['^GSPC'].Close.values,10)                     
    x = pd.DataFrame()
    y = pd.DataFrame()
    z = any
    KPI = pd.DataFrame()
    # use equal weight portfolio
    investment = 100000
    portfolio_size = len(stock_data) - 1
    investment_each = investment/portfolio_size
    
    #Loop at the stocks:
    for tick, r in stock_data.iteritems():
        f = pd.DataFrame(r)
        if tick == '^GSPC':
            continue
        else:
            #Index Close
            f['Broad_Close'] = Index_Close            
            #SMA of INDEX
            f['Broad_SMA'] = Index_MA
            #Index ADX
            f['Index ADX'] = Index_ADX
            #Bollinger bands of Index
            f['Index UPBAND'] = Index_BH
            f['Index MIDBAND'] = Index_BM
            f['Index LOWBAND'] = Index_BL
            #Bollinger bands
            bands = talib.BBANDS(r.Close.values,40,1.75,1.75)
            f['UPBAND'] = bands[0]
            f['MIDBAND'] = bands[1]
            f['LOWBAND'] = bands[2]
            #get RSI 
            f['RSI'] = talib.RSI(r.Close.values,5)
            #DI
            f['PLUS_DI'] = talib.PLUS_DI(r.High.values, r.Low.values, r.Close.values, 10)
            f['MINUS_DI'] = talib.MINUS_DI(r.High.values, r.Low.values, r.Close.values, 10)
            #get ADX 
            f['ADX'] = talib.ADX(r.High.values,r.Low.values,r.Close.values,10)        
            #get MACD 
            f['MACD'], f['SIGNAL'], f['HIST'] = talib.MACD(r.Close.values,12,26,9)
            #get Stochastic
            f['SLOWK'],f['SLOWD'] = talib.STOCH(r.High.values,r.Low.values,r.Close.values,14,3,0,3,0)
            
            #Device strategy
            M,no_of_trades,no_of_long,no_of_short,no_of_stop\
            = device_strategy(f,investment_each)
            
            #compute KPI
            if no_of_trades:
                kpi= Measure_KPI(M,tick,no_of_trades,no_of_long,no_of_short,no_of_stop)
                KPI = pd.concat([KPI,kpi],axis = 1)
            else:
                'No Trades Executed'
            x = (f.reset_index()).copy()   
            y = r.copy()
            z = tick
            
            
    print KPI        
    return x,y,z
       
            
   