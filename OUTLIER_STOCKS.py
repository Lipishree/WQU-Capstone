"""
Get the outliers as most volatile stocks
The daily change measure of each stock is calculated 
The volatility of each stock is calculated
If the daily change and volatility varies greatly, 
then they are plotted as outliers
@author: lipi
"""
import matplotlib.pyplot as plt
import numpy as np

def get_volatile_stocks(stock_data):   
    
    volatility_measure = []
    daily_change_measure = []
    labels = []
        
    for tic,data in stock_data.iteritems():
        if tic == '^GSPC':
            continue
        data['Volatility'] = (data['High'] - data['Low'])/data['Close']
        volatility_measure.append(data['Volatility'].mean())
        data['Daily_Change'] = data['Close'].diff()
        daily_change_measure.append(np.sqrt(np.mean(data['Daily_Change']**2)))       
        labels.append(tic)
        
    #Prepare plot
    plt.plot()
    plt.grid(True)
    plt.xlabel('Log of overall change metric')
    plt.ylabel('Volatility metric')
    plt.suptitle('Daily Volatility of Stocks versus Overall Trend')    
    
    #Find the Outliers
    outlier_mask = (daily_change_measure < np.percentile(daily_change_measure, 95)) & (volatility_measure < np.percentile(volatility_measure, 98))
    outliers = []
    for label, x, y, z in zip(labels, daily_change_measure, volatility_measure, outlier_mask):        
        if not z:
            outliers.append(label)
            plt.scatter(x, y, c = 'purple', cmap=plt.get_cmap('Spectral'),marker='o')
            plt.annotate(label, (x,y),color = 'red', xytext=(0,8), textcoords='offset points')
        else:
            plt.scatter(x, y, c = 'b', cmap=plt.get_cmap('Spectral'),marker='x')
            plt.annotate(label, (x,y),color = 'green', xytext=(0,8), textcoords='offset points')
    plt.show()
    
    stock_data_copy = stock_data.copy()
    for key, item in stock_data.iteritems():
        if key not in outliers and key <> '^GSPC':
            del stock_data_copy[key]  
    stock_data = stock_data_copy
    
    return outliers,stock_data