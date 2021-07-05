#CryptoWorld Project
import numpy as np
import pandas as pd


#Some given parameters. In the next time, it is tried to retrieved the most updated data.

Price_Coin = pd.read_excel (r'C:\Users\Doğan\Desktop\Doğan\Crypto_World\CoinPrices.xlsx')
BTCamount=0.00000000
ETHamount=0.00000000
LTCamount=0.00000000
BCHamount=0.00000000
XRPamount=0.00000000

BTCValue= float(Price_Coin['BTCUSD'])
ETHValue= float(Price_Coin['ETHUSD'])
LTCValue= float(Price_Coin['LTCUSD'])
BCHValue= float(Price_Coin['BCHUSD'])
XRPValue= float(Price_Coin['XRPUSD'])

#Create the wallet

MyWallet = Wallet(input("Type your username:"))
print('Welcome to the Crypto World Program.\nIn this program,you can create your wallet by investigating the parameters you would like to see.')

a=int(input('If you have some crytocurrencies, type "1" to create your wallet;\nOtherwise type "2" to create from stracth:'))

if a==1:    
    
    BTCamount=float(input('How many BTC do you have?:'))
    ETHamount=float(input('How many ETH do you have?:'))
    LTCamount=float(input('How many LTC do you have?:'))
    BCHamount=float(input('How many BCH do you have?:'))
    XRPamount=float(input('How many XRP do you have?:'))
    
    print("\nSummary of your wallet is as follows:")
    MyWallet.info()

else:
    
    print("Your account is zero now.")

#Ask whether the user will continue to trading or not
    
b=int(input("If you want to continue to trading, please type '1'; otherwise, type '2': "))

if b==2:
    
    print("\nSummary of your wallet is as follows:")
    MyWallet.info()
    
else:
    k=1
    while k>0:
        Parameter = int(input("Here is the list of parameters you can examine\n1-Historical Information, Graphics and Some Statistics\n2-Trend Analysis\n3-RSI Analysis\n4-MACD Analysis\nPlease type related number to see corresponding data:"))
        if Parameter == 1:
            coin = input("Enter the coin you would like to investigate: ")
            history = Historical_Info(coin)
        elif Parameter == 2:
            coin = input("Enter the coin you would like to investigate: ")
            trend = Trend_Analysis(coin)
        elif Parameter == 3:
            print("RSI ekle")
        else:
            print("MACD Analysis will be loaded to the program soon!")
        k=int(input("If you would like to investigate another coin or parameter, please type '1'; otherwise, type '0' to update your wallet!:"))
 
 
#Ask for buying / selling cryptocurrencies and update the wallet




 
