"""
Get historical data of stocks
@author: lipi
"""
import datetime
from pandas.io import data

def fetch_stock_hist_data(stocks):
    #Enter the stocks you wish to use 
    date1 = datetime.date.today() #today
    end= date1
    start = date1.replace(year=date1.year - 1)
    start_str = '{:%Y%m%d}'.format(start)
    end_str = '{:%Y%m%d}'.format(end)
    all_data = {}
    i = 0
    for ticker in stocks:
        i+=1
        try:
            all_data[ticker] = data.get_data_yahoo(ticker,start_str,end_str)   
        except IOError:
            continue
    return all_data 
