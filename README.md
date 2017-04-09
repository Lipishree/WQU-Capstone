This repository is created as part of CAPSTONE project submission for WQU 2015-2017
It contains python sample code, that demonstrates short-term trading using a combination of monentum, volatility and trend indicators
                                                            
                                                            
      > CAPSTONE.py is the Main program
      
      > CAP_STCK_ENTRY This module allows user to enter his choice of stock through file or enter tickers manually on screen
  
      > STOCK_DATA This This module fetches the historical data of the tickers entered above
  
      > OUTLIER_STOCKS This module gets the most volatile stock among the lot and plots the same
  
      > SIGNAL_FILTERS Computes the Indicators. TA-Lib library is used for the same [1]
  
      > STRATEGY_ADX_BB_MACD_RSI This module has the trading strategy that uses MACD,RSI,ADX and Bollinger Bands to enter long or short             positions. Slippage, Brokerage and Stop Loss are also available here 
      
      > KEY_PROCESS_INDICATORS KPI is calculates here and displayed on user screen
      
      > PLOT_INDICATORS The Stock data along with the indicators are plotted for user refrence
  
  [1]From [http://www.lfd.uci.edu/~gohlke/pythonlibs/]
     downloaded and installed [pycuda 2016.1.2+cuda7518 cp27 cp27m win_amd64.whl] that fetches all the Indicators
