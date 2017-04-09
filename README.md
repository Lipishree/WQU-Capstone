This repository is created as part of CAPSTONE project submission for WQU 2015-2017
It contains python sample code, that demonstrates short-term trading using a combination of monentum, volatility and trend indicators
                                                            
                                                            
      CAPSTONE is the Main program
      
      CAP_STCK_ENTRY This module allows user to enter his choice of stock through file or enter tickers manually on screen
      
      STOCK_DATA This This module fetches the historical data of the tickers entered above
      
      OUTLIER_STOCKS This module gets the most volatile stock among the lot and plots the same
      
      SIGNAL_FILTERS Computes the Indicators. TA-Lib library is used for the same [1]
      
      STRATEGY_ADX_BB_MACD_RSI This module has the trading strategy that uses MACD,RSI,ADX and Bollinger Bands to enter long or short
      
      KEY_PROCESS_INDICATORS KPI is calculates here and displayed on user screen
      
      PLOT_INDICATORS The Stock data along with the indicators are plotted for user refrence
  
  [1]From [http://www.lfd.uci.edu/~gohlke/pythonlibs/]
     downloaded and installed [pycuda 2016.1.2+cuda7518 cp27 cp27m win_amd64.whl] that fetches all the Indicators

Strategy:
Entering Long Positions:

1.	When the MACD has crossed the signal line from above to down
2.	When RSI crosses above 30 from below
3.	When ADX of both Stock and Broader Market is above 25
4.	Close has fallen below Lower Bollinger Band	

Entering Short Positions:

1.	When the MACD has crossed the signal line from down to above
2.	When RSI crosses below 70 from above
3.	When ADX of both Stock and Broader Market is above 25
4.	Close has risen above Bollinger Band

Exiting Long:

When the close touches or crosses the upper Bollinger band

Exiting Short:

When the close touches or crosses the lower Bollinger band

Stop Loss:
While holding long or short, if the price falls further or rises up, a stop loss should be in place to minimize the losses. We use here, 5% of the Close. If while holding Long, the price falls further then Execute stop-loss at 5% less than current Close. While holding short, execute stop-loss at 5% higher than current Close. 
The 5% has been decided by trial and error method in running the simulation 
Brokerage:

A standard brokerage charge per share is considered assuming trading on ‘Lightspeed trading’

Slippage:

Slippage percentage is calculated by dividing "d1," the distance between the theoretical order entry price and the actual fill price, by "d2," the distance between the theoretical order price and the worst possible fill price. As an example, consider the following for a "buy" order:
Theoretical entry price: 1060
Actual fill price: 1064
Bar high (worst possible) long entry price: 1100
d1 = 1064 - 1060 = 4
d2 = 1100 - 1060 = 40
Slippage = d1 / d2 = 4 / 40 = 10%
Once the slippage is calculated, in our back-testing, we assume that we are buying a stock considering the slippage:
P` = P +/- (P * Slippage)    #Depending on Long or /Short entry
The brokerage and slippage is very important in short-term trading because, the positions are entered and exited frequently over short period of time and each stock encounters slippage and brokerage. If we don’t use slippage and brokerage in simulation, then we might get great profits, but in reality we might not be benefiting with the brokerage and slippage in place.  So, back testing with these is very important 

