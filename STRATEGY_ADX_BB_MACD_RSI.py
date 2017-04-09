"""
@author: lipi
Device Strategy for short-term trading
1. If RSI crosses 30 from Below and
      MACD cosses Signal from above and
      Both Stock and Broad Market ADX is above 25 and
      Close is less than Lower Bollinger Band
      Go Long
2. If RSI crosses 70 from Above and
      MACD cosses Signal from below and
      Both Stock and Broad Market ADX is above 25 and
      Close is greater than Upper Bollinger Band
      Go Long  
3. Exit trades when price touches the opposite band
4. Stop loss if Price rises or falls above or below 5% of its own value
5. Exit when we reach the end      
     
"""

def device_strategy(data,cash):
    x = data.dropna().copy()
    x = (x.reset_index())
    pos = 'None'
    macd_cross = 'None'
    pnl = []
    stop = 0
    longs = 0
    short = 0
    brokerage_per = 0.0045
    trades = 0
    
    for i in range(0,len(x)):
        pct_change = 0
        #Taking Positions===============================================
        if x.iloc[i-1]['MACD'] < x.iloc[i-1]['SIGNAL']\
        and x.iloc[i]['MACD'] > x.iloc[i]['SIGNAL']:
            macd_cross = 'Up'
        if x.iloc[i-1]['MACD'] > x.iloc[i-1]['SIGNAL']\
        and x.iloc[i]['MACD'] < x.iloc[i]['SIGNAL']:
            macd_cross = 'Down'  
            
        if pos == 'None' and i > 1:
                #Slippage
                d1 = x.iloc[i]['Open'] - x.iloc[i-1]['Close']
                d2 = x.iloc[i]['High'] - x.iloc[i-1]['Close']
                if d2 == 0:
                    d2 = d1
                    
                if x.iloc[i-1]['RSI'] <= 30 and x.iloc[i]['RSI'] > 30:#RSI cross 30 from below
                    if macd_cross == 'Down' and x.iloc[i]['MACD'] < x.iloc[i]['SIGNAL']:
                        if x.iloc[i]['ADX'] > 25 and x.iloc[i]['Index ADX'] > 25: 
                            if x.iloc[i-1]['Close'] < x.iloc[i-1]['LOWBAND']:#Candle-Stick Close below Lower Bollinger Band
                                #Go Long-----------------------------------
                                pos = 'Long'
                                P = x.iloc[i-1]['Close']
                                Slippage = (d1 / d2)/100
                                P = P + (P*Slippage) + brokerage_per
                                position = cash/P
                                cash = cash - (P*position)
                                trades+=1
                                longs+=1
                if x.iloc[i-1]['RSI'] >= 70 and x.iloc[i]['RSI'] < 70:#RSI cross 70 from above
                    if macd_cross == 'Up' and x.iloc[i]['MACD'] > x.iloc[i]['SIGNAL']:
                        if x.iloc[i]['ADX'] > 25 and x.iloc[i]['Index ADX'] > 25:
                            if x.iloc[i-1]['Close'] > x.iloc[i-1]['UPBAND']:#Candle-Stick Close above Upper Bollinger Band
                                #Go Short-----------------------------------
                                pos = 'Short'
                                S = x.iloc[i-1]['Close']
                                Slippage = (d1 / d2)/100
                                S = S + (S*Slippage) - brokerage_per
                                position = cash/S
                                cash = cash + (S*position)
                                trades+=1
                                short+=1
        #Exit Strategy================================================
        if pos == 'Long':
            stop_down = P - (P*0.05)
            if x.iloc[i-1]['Close'] >= x.iloc[i]['UPBAND']:
                #Exit Position by locking profit------------------
                pos = 'None'
                S = x.iloc[i-1]['Close']
                Slippage = (d1 / d2)/100
                S = S + (S*Slippage) - brokerage_per
                cash = cash + (S*position)
                pct_change =  (S/P-1)
                position = 0
            elif P > x.iloc[i-1]['Close']:
                if x.iloc[i-1]['Close'] <= stop_down:
                    #Exit Position by Stop Loss-------------------------
                    pos = 'None'
                    Slippage = (d1 / d2)/100
                    SL = stop_down + (stop_down*Slippage) - brokerage_per
                    pct_change =  (SL/P-1)
                    cash = cash + (SL*position)
                    position = 0
                    stop+=1
        if pos == 'Short':
            stop_up = S + (S*0.05)
            if x.iloc[i-1]['Close'] <= x.iloc[i]['LOWBAND']:
                #Exit Position by locking profit--------------------
                pos = 'None'
                P = x.iloc[i-1]['Close']
                Slippage = (d1 / d2)/100
                P = P + (P*Slippage) + brokerage_per
                cash = cash - (P*position)
                pct_change =  (S/P-1)
                position = 0
            elif S < x.iloc[i-1]['Close']:
                if x.iloc[i-1]['Close'] >= stop_up:
                    #Exit Position by Stop Loss--------------------------
                    pos = 'None'
                    Slippage = (d1 / d2)/100
                    SL = stop_up + (stop_up*Slippage) + brokerage_per
                    pct_change =  (S/SL-1)
                    cash = cash - (SL*position)
                    position = 0
                    stop+=1
        if i == len(x) - 1 and pos <> 'None':
            E = x.iloc[i-1]['Close']
            if pos == 'Long':
               Slippage = (d1 / d2)/100
               E = E + (E*Slippage) - brokerage_per
               pct_change =  (E/P-1)
               cash = cash + (E*position)
            if pos == 'Short':
               Slippage = (d1 / d2)/100
               E = E + (E*Slippage) + brokerage_per
               pct_change =  (S/E-1)
               cash = cash - (E*position)
            position = 0
            pos = 'None'
            
        pnl.append(pct_change) 
    x['PnL'] = pnl
    
    return x,trades,longs,short,stop   
            