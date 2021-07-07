#CryptoWorld Project
import numpy as np
import pandas as pd


#Some given parameters. In the next time, it is tried to retrieved the most updated data.

coinlist = ['BTC', 'ETH', 'LTC', 'BCH', 'XRP']
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

TotalCommission = 0
commission = [25.0, 8.0, 4.03, 1.28, 0.25] #☻commission prices in dollars per 1 unit currency.

#Create the wallet
user = input("Type your username:")
MyWallet = Wallet(user)
print(f'Welcome to the Crypto World Program {user}.\nIn this program,you can create your wallet by investigating the parameters you would like to see.')

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
    
b=int(input("If you want to investigate cryptocurrencies, please type '1'; otherwise, type '2': "))

if b==1:

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
            rsi = RSI_Analysis(b)
        else:
            macd = MACD_Analysis(b)
            print("MACD Analysis will be loaded to the program soon!")
        k=int(input("If you would like to investigate another coin or parameter, please type '1'; otherwise, type '0' to update your wallet!:"))
 

#Ask for buying / selling cryptocurrencies and update the wallet

BTCchange = 0
ETHchange = 0
LTCchange = 0
BCHchange = 0
XRPchange = 0

# for buying

buysell = int(input('Do you want to buy any coin? (1 for Yes), (0 for No):'))

while buysell > 0:
    buycoin = input(f'Which coin do you want to buy from the below list?\n{coinlist}\n')
    if buycoin == 'BTC':
        BTCold = BTCamount
        BTCbuyamount = float(input('How many BTC will you buy?:'))
        BTCamount += BTCbuyamount
        BTCchange = BTCamount - BTCold
        TotalCommission += BTCbuyamount*commission[0]
    elif buycoin == 'ETH':
        ETHold = ETHamount
        ETHbuyamount = float(input('How many ETH will you buy?:'))
        ETHamount += ETHbuyamount
        ETHchange = ETHamount - ETHold
        TotalCommission += ETHbuyamount*commission[1]            
    elif buycoin == 'LTC':
        LTCold = LTCamount
        LTCbuyamount = float(input('How many LTC will you buy?:'))
        LTCamount += LTCbuyamount
        LTCchange = LTCamount - LTCold
        TotalCommission += LTCbuyamount*commission[2]              
    elif buycoin == 'BCH':
        BCHold = BCHamount
        BCHbuyamount = float(input('How many BCH will you buy?:'))
        BCHamount += BCHbuyamount
        BCHchange = BCHamount - BCHold
        TotalCommission += BCHbuyamount*commission[3]  
    else:
        XRPold = XRPamount
        XRPbuyamount = float(input('How many XRP will you buy?:'))
        XRPamount += XRPbuyamount
        XRPchange = XRPamount - XRPold
        TotalCommission += XRPbuyamount*commission[4]  
    buysell = int(input('Do you want to buy another coin? (1 for Yes), (0 for No):'))

# for selling

buysell = int(input('Do you want to sell any coin? (1 for Yes), (0 for No):'))

while buysell > 0:
    sellcoin = input(f'Which coin do you want to sell from the below list?\n{coinlist}\n')
    if sellcoin == 'BTC':
        BTCold = BTCamount
        BTCsellamount = float(input('How many BTC will you sell?:'))
        BTCamount -= BTCsellamount
        BTCchange = BTCamount - BTCold
        TotalCommission += BTCsellamount*commission[0]
    elif sellcoin == 'ETH':
        ETHold = ETHamount
        ETHsellamount = float(input('How many ETH will you sell?:'))
        ETHamount -= ETHsellamount
        ETHchange = ETHamount - ETHold
        TotalCommission += ETHsellamount*commission[1]            
    elif sellcoin == 'LTC':
        LTCold = LTCamount
        LTCsellamount = float(input('How many LTC will you sell?:'))
        LTCamount -= LTCsellamount
        LTCchange = LTCamount - LTCold
        TotalCommission += LTCsellamount*commission[2]              
    elif buycoin == 'BCH':
        BCHold = BCHamount
        BCHsellamount = float(input('How many BCH will you sell?:'))
        BCHamount -= BCHsellamount
        BCHchange = BCHamount - BCHold
        TotalCommission += BCHsellamount*commission[3]  
    else:
        XRPold = XRPamount
        XRPsellamount = float(input('How many XRP will you sell?:'))
        XRPamount -= XRPsellamount
        XRPchange = XRPamount - XRPold
        TotalCommission += XRPsellamount*commission[4]  
    buysell = int(input('Do you want to sell another coin? (1 for Yes), (0 for No):'))           
            

#Last Summary

print("The amount of Bitcoin in your wallet has changed by", BTCchange)
print("\nThe amount of Ethereum in your wallet has changed by", ETHchange)
print("\nThe amount of Litecoin in your wallet has changed by", LTCchange)
print("\nThe amount of Bitcoin Cash in your wallet has changed by", BCHchange)
print("\nThe amount of Ripple in your wallet has changed by", XRPchange)


print("Your updated wallet is\n")

MyUpdatedWallet = Wallet(user)
MyUpdatedWallet.info()   

print("\nTotal Commission is equal to", TotalCommission)  
