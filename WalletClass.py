
#Wallet of the user

class Wallet(object):  
    
    
    def __init__(self, name):
        self.UserName = name     
 
        
    def info(self):

        print(f'Username: {self.UserName}')
 
        if BTCamount:
            self.TotalValueBTC = BTCamount*BTCValue
            print(f'You have {BTCamount} BTC and its total value is ${self.TotalValueBTC}.')
        else:
            self.TotalValueBTC = 0

        if ETHamount:
            self.TotalValueETH = ETHamount*ETHValue
            print(f'You have {ETHamount} ETH and its total value is ${self.TotalValueETH}.')
        else:
            self.TotalValueETH = 0
            
        if LTCamount:
            self.TotalValueLTC = LTCamount*LTCValue
            print(f'You have {LTCamount} LTC and its total value is ${self.TotalValueLTC}.')
        else:
            self.TotalValueLTC = 0
            
        if BCHamount:
            self.TotalValueBCH = BCHamount*BCHValue
            print(f'You have {BCHamount} BCH and its total value is ${self.TotalValueBCH}.')
        else:
            self.TotalValueBCH = 0
            
        if XRPamount:
            self.TotalValueXRP = XRPamount*XRPValue
            print(f'You have {XRPamount} XRP and its total value is ${self.TotalValueXRP}.')
        else:
            self.TotalValueXRP = 0
            
        print(f'Total Value of your wallet is ${self.TotalValueBTC + self.TotalValueETH + self.TotalValueLTC + self.TotalValueBCH + self.TotalValueXRP}')
