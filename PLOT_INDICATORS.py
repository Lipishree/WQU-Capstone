"""
@author: lipi
Plot Candlesticks
Bollinger Bands
ADX
RSI
MACD
"""

import pandas            as pd
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.dates    import date2num
from matplotlib.finance  import _candlestick as candlestick

def plot_signals_and_indicators(tick,data,inddata):
    f,ax=plt.subplots(4,1,sharex=True) 
    f.subplots_adjust(hspace=0.05)
    gs = GridSpec(4, 1,height_ratios=[6,2,2,2])
    plt.xticks(rotation=70)
    plt.grid(True)
    twentyfive =  [25.00] * len(inddata['Date'])
    thirty     =  [30.00] * len(inddata['Date'])
    fourty     =  [40.00] * len(inddata['Date'])
    fifty      =  [50.00] * len(inddata['Date'])
    seventy    =  [70.00] * len(inddata['Date'])
               
    ax[0] = plt.subplot(gs[0])
    ax[1] = plt.subplot(gs[1])
    ax[2] = plt.subplot(gs[2],sharex = ax[1])
    ax[3] = plt.subplot(gs[3],sharex = ax[1])
    
    ax[0].set_axis_bgcolor('black')
    ax[1].set_axis_bgcolor('black')
    ax[2].set_axis_bgcolor('black')
    ax[3].set_axis_bgcolor('black')
    
    #Plotting the data 
    stck_data = pd.DataFrame(data)
    stck_data['Date'] = date2num(stck_data.index.to_pydatetime())
    candlesticks = [tuple(x) for x in stck_data[['Date', 'Open', 'Close', 'High', 'Low']].to_records(index=False)]
    candlestick(ax[0], candlesticks,width=0.5, colorup='white', colordown='cyan')
    ax[0].set_title(tick.upper())
    
    #Plotting Bollinger Bands
    ax[0].plot(inddata['Date'],inddata['LOWBAND'],color = 'red',label= 'Bollinger Lower Band')
    ax[0].plot(inddata['Date'],inddata['UPBAND'],color = 'green',label= 'Bollinger Upper Band')
    ax[0].plot(inddata['Date'],inddata['MIDBAND'],color = 'blue',label= 'Simple Moving Average')
    ax[3].set_xticklabels(ax[0].xaxis.get_majorticklabels(),rotation=45) 
    ax[0].get_xaxis().set_visible(False)
    ax[0].legend(loc='upper left', shadow=True)
    
    #Plotting ADX
    ax[1].plot(inddata['Date'],inddata['ADX'],label = 'ADX')        
    ax[1].plot(inddata['Date'],fourty,'--',color = 'mediumvioletred')
    ax[1].plot(inddata['Date'],twentyfive,'--',color = 'mediumvioletred')
    ax[1].get_xaxis().set_visible(False)
    ax[1].legend(loc='upper left', shadow=True)
    
    #Plotting RSI
    ax[2].plot(inddata['Date'],inddata['RSI'],label='RSI')
    ax[2].plot(inddata['Date'],fifty,'--',color = 'red')
    ax[2].plot(inddata['Date'],thirty,'--',color = 'yellow')
    ax[2].fill_between(data['Date'],thirty, inddata['RSI'],color = 'lawngreen')
    ax[2].fill_between(data['Date'],thirty, seventy,color = 'black')
    ax[2].plot(inddata['Date'],seventy,'--', color = 'yellow')
    ax[2].get_xaxis().set_visible(False)
    ax[2].legend(loc='upper left', shadow=True)
    
    #Plotting MACD
    ax[3].plot(inddata['Date'],inddata['MACD'],color = 'orange',linewidth = 2,label='MACD') 
    ax[3].plot(inddata['Date'],inddata['SIGNAL'],color = 'grey',linewidth = 2,label='SIGNAL')
    ax[3].bar(data['Date'],inddata['HIST'],width = 1,color = 'yellow',linewidth=0)       
    ax[3].set_xlabel('Date')      
    ax[3].legend(loc='upper left', shadow=True)
    
    
    f1,axx =plt.subplots(4,1,sharex=True)
    
    axx[0].set_axis_bgcolor('grey')
    axx[1].set_axis_bgcolor('grey')
    axx[2].set_axis_bgcolor('silver')
    axx[3].set_axis_bgcolor('silver')    
    
    #Plotting Broader Market
    axx[0].set_title('BROAD MARKET TREND')
    axx[0].plot(inddata['Date'],inddata['Broad_Close'],color = 'black',label='_nolegend_')
    axx[0].plot(inddata['Date'],inddata['Index UPBAND'],color = 'green',label= 'Upper BBand')
    axx[0].plot(inddata['Date'],inddata['Index MIDBAND'],color = 'blue',label='_nolegend_')
    axx[0].plot(inddata['Date'],inddata['Index LOWBAND'],color = 'red',label= 'Lower BBand')
    axx[0].get_xaxis().set_visible(False)
    axx[0].legend(loc='upper left', shadow=True)
    
    #Plotting ADX
    axx[1].plot(inddata['Date'],inddata['Index ADX'],label = 'ADX')        
    axx[1].plot(inddata['Date'],fourty,'--',color = 'mediumvioletred')
    axx[1].plot(inddata['Date'],twentyfive,'--',color = 'mediumvioletred')
    axx[1].get_xaxis().set_visible(False)
    axx[1].legend(loc='upper left', shadow=True)
    
    #Plotting ADX
    axx[2].set_title(tick.upper())
    axx[2].plot(inddata['Date'],inddata['ADX'],label = 'ADX')       
    axx[2].plot(inddata['Date'],fourty,'--',color = 'mediumvioletred')
    axx[2].plot(inddata['Date'],twentyfive,'--',color = 'mediumvioletred')
    axx[2].get_xaxis().set_visible(False)
    axx[2].legend(loc='upper left', shadow=True)
    
    #Plot Stock
    axx[3].plot(inddata['Date'],inddata['Close'],color = 'black',label='_nolegend_')
    axx[3].plot(inddata['Date'],inddata['LOWBAND'],color = 'red',label= 'Lower BBand')
    axx[3].plot(inddata['Date'],inddata['UPBAND'],color = 'green',label= 'Upper BBand')
    axx[3].plot(inddata['Date'],inddata['MIDBAND'],color = 'blue',label='_nolegend_')
    axx[3].set_xticklabels(ax[0].xaxis.get_majorticklabels(),rotation=45)  
    axx[3].legend(loc='upper left', shadow=True)
    
    
       