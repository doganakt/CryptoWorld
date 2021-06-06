#Wallet of the user

class Wallet(object):  
    
    
    def __init__(self, name):
        self.UserName = name     
 
        
    def info(self):

        print(f'Username: {self.UserName}')
 
        if BTCamount:
            self.TotalValueBTC = BTCamount*BTCValue
            print(f'You have {BTCamount} BTC and its total value is ${self.TotalValueBTC}.')

        if ETHamount:
            self.TotalValueETH = ETHamount*ETHValue
            print(f'You have {ETHamount} ETH and its total value is ${self.TotalValueETH}.')
        print(f'Total Value of your wallet is ${self.TotalValueBTC +self. TotalValueETH}')
