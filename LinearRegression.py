#Linear Regression Analysis

import pandas as pd
import numpy as np

def Trend_Analysis(coinselection):

    
    if coinselection == 'BTC':
        
        #Retrieve data 
        
        BTCread = pd.read_excel (r'C:\Users\Doğan\Desktop\Doğan\Crypto_World\BTC-USD.xlsx')
        BTCcloses=BTCread['Adj Close']
        
        term = input('Which horizon would you like to see the trend on?:\n-3 months\n-6 months\n-1 year\nHorizon:')
        if term == '3 months':
            data_y = np.zeros(12)
            for i in range(12): 
                data_y[-i] = BTCcloses[len(BTCcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in short term is up, buying Bitcoin seems reasonable!")
            else:
                print("Trend in short term is down, buying Bitcoin is not suggested!")
                
        elif term == '6 months':
            data_y = np.zeros(24)
            for i in range(24): 
                data_y[-i] = BTCcloses[len(BTCcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in middle term is up, buying Bitcoin seems reasonable!")
            else:
                print("Trend in middle term is down, buying Bitcoin is not suggested!")
                
        else:
            data_y = np.zeros(52)
            for i in range(52): 
                data_y[-i] = BTCcloses[len(BTCcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in long term is up, buying Bitcoin seems reasonable!")
            else:
                print("Trend in long term is down, buying Bitcoin is not suggested!")

    elif coinselection == 'ETH':
        
        #Retrieve data 
        
        ETHread = pd.read_excel (r'C:\Users\Doğan\Desktop\Doğan\Crypto_World\ETH-USD.xlsx')
        ETHcloses=ETHread['Adj Close']
        
        term = input('Which horizon would you like to see the trend on?:\n-3 months\n-6 months\n-1 year\nHorizon:')
        if term == '3 months':
            data_y = np.zeros(12)
            for i in range(12): 
                data_y[-i] = ETHcloses[len(ETHcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in short term is up, buying Ethereum seems reasonable!")
            else:
                print("Trend in short term is down, buying Ethereum is not suggested!")
                
        elif term == '6 months':
            data_y = np.zeros(24)
            for i in range(24): 
                data_y[-i] = ETHcloses[len(ETHcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in middle term is up, buying Ethereum seems reasonable!")
            else:
                print("Trend in middle term is down, buying Ethereum is not suggested!")
                
        else:
            data_y = np.zeros(52)
            for i in range(52): 
                data_y[-i] = ETHcloses[len(ETHcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in long term is up, buying Ethereum seems reasonable!")
            else:
                print("Trend in long term is down, buying Ethereum is not suggested!")

    elif coinselection == 'LTC':
        
        #Retrieve data 
        
        LTCread = pd.read_excel (r'C:\Users\Doğan\Desktop\Doğan\Crypto_World\LTC-USD.xlsx')
        LTCcloses=LTCread['Adj Close']
        
        term = input('Which horizon would you like to see the trend on?:\n-3 months\n-6 months\n-1 year\nHorizon:')
        if term == '3 months':
            data_y = np.zeros(12)
            for i in range(12): 
                data_y[-i] = LTCcloses[len(LTCcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in short term is up, buying Litecoin seems reasonable!")
            else:
                print("Trend in short term is down, buying Litecoin is not suggested!")
                
        elif term == '6 months':
            data_y = np.zeros(24)
            for i in range(24): 
                data_y[-i] = LTCcloses[len(LTCcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in middle term is up, buying Litecoin seems reasonable!")
            else:
                print("Trend in middle term is down, buying Litecoin is not suggested!")
                
        else:
            data_y = np.zeros(52)
            for i in range(52): 
                data_y[-i] = LTCcloses[len(LTCcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in long term is up, buying Litecoin seems reasonable!")
            else:
                print("Trend in long term is down, buying Litecoin is not suggested!")    

    elif coinselection == 'BCH':
        
        #Retrieve data 
        
        BCHread = pd.read_excel (r'C:\Users\Doğan\Desktop\Doğan\Crypto_World\BCH-USD.xlsx')
        BCHcloses=BCHread['Adj Close']
        
        term = input('Which horizon would you like to see the trend on?:\n-3 months\n-6 months\n-1 year\nHorizon:')
        if term == '3 months':
            data_y = np.zeros(12)
            for i in range(12): 
                data_y[-i] = BCHcloses[len(BCHcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in short term is up, buying Bitcoin Cash seems reasonable!")
            else:
                print("Trend in short term is down, buying Bitcoin Cash is not suggested!")
                
        elif term == '6 months':
            data_y = np.zeros(24)
            for i in range(24): 
                data_y[-i] = BCHcloses[len(BCHcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in middle term is up, buying Bitcoin Cash seems reasonable!")
            else:
                print("Trend in middle term is down, buying Bitcoin Cash is not suggested!")
                
        else:
            data_y = np.zeros(52)
            for i in range(52): 
                data_y[-i] = BCHcloses[len(BCHcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in long term is up, buying Bitcoin Cash seems reasonable!")
            else:
                print("Trend in long term is down, buying Bitcoin Cash is not suggested!") 

    else: 
        
        #Retrieve data 
        
        XRPread = pd.read_excel (r'C:\Users\Doğan\Desktop\Doğan\Crypto_World\XRP-USD.xlsx')
        XRPcloses=XRPread['Adj Close']
        
        term = input('Which horizon would you like to see the trend on?:\n-3 months\n-6 months\n-1 year\nHorizon:')
        if term == '3 months':
            data_y = np.zeros(12)
            for i in range(12): 
                data_y[-i] = XRPcloses[len(XRPcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in short term is up, buying Ripple seems reasonable!")
            else:
                print("Trend in short term is down, buying Ripple is not suggested!")
                
        elif term == '6 months':
            data_y = np.zeros(24)
            for i in range(24): 
                data_y[-i] = XRPcloses[len(XRPcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in middle term is up, buying Ripple seems reasonable!")
            else:
                print("Trend in middle term is down, buying Ripple is not suggested!")
                
        else:
            data_y = np.zeros(52)
            for i in range(52): 
                data_y[-i] = XRPcloses[len(XRPcloses)-i-1]
                data_x = np.arange(0,len(data_y))

            z = np.polyfit(data_x,data_y,1)
            print(z[0])
            if z[0] >= 0:
                print("Trend in long term is up, buying Ripple seems reasonable!")
            else:
                print("Trend in long term is down, buying Ripple is not suggested!") 
