#CryptoWorld Project
import numpy as np
import pandas as np

#Some given parameters. In the next time, it is tried to retrieved the most updated data.

BTCamount=0
ETHamount=0
BTCValue=5
ETHValue=2

#Create the wallet

MyWallet = Wallet(input("Type your username:"))
print('Welcome to the Crypto World Program.\nIn this program,you can create your wallet by investigating the parameters you would like to see.')

a=int(input('If you have some crytocurrencies, type "1" to create your wallet;\nOtherwise type "2" to create from stracth:'))

if a==1:    
    
    BTCamount=float(input('How many BTC do you have?:'))
    ETHamount=float(input('How many ETH do you have?:'))
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
        print("Here is the list of data you can see\nPlease type related number to see corresponding data:")
        deneme = Historical_Info('BTC')
        k=0
