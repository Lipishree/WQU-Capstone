"""
Get historical data of stocks
from Yahoo Finanace using the tickers entered
@author: lipi
"""
import datetime
from pandas.io import data

def fetch_stock_hist_data(stocks): 
    date1 = datetime.date.today() #today
    end= date1
    start = date1.replace(year=date1.year - 1)#Fetch the data of past one year
    start_str = '{:%Y%m%d}'.format(start)
    end_str = '{:%Y%m%d}'.format(end)
    all_data = {}
    i = 0
    for ticker in stocks:
        i+=1
        try:
            #Get data from Yahoo Finance
            all_data[ticker] = data.get_data_yahoo(ticker,start_str,end_str)   
        except IOError:
            continue
    return all_data 
