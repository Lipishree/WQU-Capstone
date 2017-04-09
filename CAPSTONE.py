"""

This short term trading strategy follows the following steps 
to device the strategy and output the results

1.Enter the preffered stock combinations
2.Fetch Historical data
3.Identify Volatile stocks
4.Device Short Term Trading startegy
5Plot and display data

@author: lipi
"""
#Imports
from CAP_STCK_ENTRY import stock_entry_option
from STOCK_DATA import fetch_stock_hist_data
from OUTLIER_STOCKS import get_volatile_stocks
from SIGNAL_FILTERS import mean_reversion_and_trading_strategy
from PLOT_INDICATORS import plot_signals_and_indicators
 
#Main Program   
if __name__ == '__main__':
    #Get Stock list
    tickers = stock_entry_option()
    #Get stock historical data
    data = fetch_stock_hist_data(tickers)
    #Get most volatile stocks
    volatile,data = get_volatile_stocks(data)
    # Get Indicators for trading
    indicators,data,tic = mean_reversion_and_trading_strategy(data)
    #Plot the stock data and the indicators
    plot_signals_and_indicators(tic,data,indicators)
    
    
    

