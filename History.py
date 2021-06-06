#Analyze the historical data


from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from IPython.display import display



def Historical_Info(selection):
  
# if BTC is requested

    if selection=='BTC':

        # Read the files
        
        BTCread = pd.read_excel (r'C:\Users\Doğan\Desktop\Doğan\Crypto_World\BTC-USD.xlsx')
        BTCcloses=BTCread['Adj Close']
        Date=BTCread['Date']

        # Plot the historical data

        fig, ax = plt.subplots(figsize=(19, 5))
        fig.subplots_adjust(bottom=0.15, left=0.2)
        ax.plot(Date, BTCcloses)
        ax.set_xlabel('Date [in weeks]',size=15)
        ax.set_ylabel('BTC Values ($)',size=15)
        ax.set_title('Weekly BTC-USD Graph for last 3 years', size=15, fontweight='bold')
        plt.show()

        # Give some hints to the user

        BTCaverage = np.average(BTCcloses)
        BTCmax = max(BTCcloses)
        BTCvalue6months=BTCcloses[len(Date)-23]
        BTCtable={'Statistics' : ['The Last Week Close', 'Average($)', 'ATH($)', 'Increase in last 3 years(%)', 'Increase in last 6 months(%)'],
                  'Values' : [BTCcloses[len(Date)-1], BTCaverage, BTCmax, 100*(BTCcloses[len(Date)-1]-BTCcloses[0])/BTCcloses[0], 100*(BTCcloses[len(Date)-1]-BTCvalue6months)/BTCvalue6months]
                  }
        display(pd.DataFrame(BTCtable))


# if ETH is requested

    elif selection=='ETH':
        
        # Read the files
        
        ETHread = pd.read_excel (r'C:\Users\Doğan\Desktop\Doğan\Crypto_World\ETH-USD.xlsx')
        ETHcloses=ETHread['Adj Close']


        # Plot the historical data

        fig, ax = plt.subplots(figsize=(19, 5))
        fig.subplots_adjust(bottom=0.15, left=0.2)
        ax.plot(Date, ETHcloses)
        ax.set_xlabel('Date [in weeks]',size=15)
        ax.set_ylabel('ETH Values ($)',size=15)
        ax.set_title('Weekly ETH-USD Graph for last 3 years', size=15, fontweight='bold')
        plt.show()

        # Give some hints to the user

        ETHaverage = np.average(ETHcloses)
        ETHmax = max(ETHcloses)
        ETHvalue6months=ETHcloses[len(Date)-23]
        ETHtable={'Statistics' : ['The Last Week Close', 'Average($)', 'ATH($)', 'Increase in last 3 years(%)', 'Increase in last 6 months(%)'],
                  'Values' : [ETHcloses[len(Date)-1], ETHaverage, ETHmax, 100*(ETHcloses[len(Date)-1]-ETHcloses[0])/ETHcloses[0], 100*(ETHcloses[len(Date)-1]-ETHvalue6months)/ETHvalue6months]
                  }
        display(pd.DataFrame(ETHtable))

# if BNB is requested

    elif selection=='BNB':  
        
        # Read the files
        
        BNBread = pd.read_excel (r'C:\Users\Doğan\Desktop\Doğan\Crypto_World\BNB-USD.xlsx')
        BNBcloses=BNBread['Adj Close']

        # Plot the historical data

        fig, ax = plt.subplots(figsize=(19, 5))
        fig.subplots_adjust(bottom=0.15, left=0.2)
        ax.plot(Date, BNBcloses)
        ax.set_xlabel('Date [in weeks]',size=15)
        ax.set_ylabel('BNB Values ($)',size=15)
        ax.set_title('Weekly BNB-USD Graph for last 3 years', size=15, fontweight='bold')
        plt.show()

        # Give some hints to the user
        
        BNBaverage = np.average(BNBcloses)
        BNBmax = max(BNBcloses)
        BNBvalue6months=BNBcloses[len(Date)-23]
        BNBtable={'Statistics' : ['The Last Week Close', 'Average($)', 'ATH($)', 'Increase in last 3 years(%)', 'Increase in last 6 months(%)'],
                'Values' : [BNBcloses[len(Date)-1], BNBaverage, BNBmax, 100*(BNBcloses[len(Date)-1]-BNBcloses[0])/BNBcloses[0], 100*(BNBcloses[len(Date)-1]-BNBvalue6months)/BNBvalue6months]
                }
        display(pd.DataFrame(BNBtable))

# if ADA is requested

    elif selection=='ADA':
        
        # Read the files
        
        ADAread = pd.read_excel (r'C:\Users\Doğan\Desktop\Doğan\Crypto_World\ADA-USD.xlsx')
        ADAcloses=ADAread['Adj Close']
              
        # Plot the historical data
        
        fig, ax = plt.subplots(figsize=(19, 5))
        fig.subplots_adjust(bottom=0.15, left=0.2)
        ax.plot(Date, ADAcloses)
        ax.set_xlabel('Date [in weeks]',size=15)
        ax.set_ylabel('ADA Values ($)',size=15)
        ax.set_title('Weekly ADA-USD Graph for last 3 years', size=15, fontweight='bold')
        plt.show()
        
        # Give some hints to the user
        
        ADAaverage = np.average(ADAcloses)
        ADAmax = max(ADAcloses)
        ADAvalue6months=ADAcloses[len(Date)-23]
        ADAtable={'Statistics' : ['The Last Week Close', 'Average($)', 'ATH($)', 'Increase in last 3 years(%)', 'Increase in last 6 months(%)'],
                'Values' : [ADAcloses[len(Date)-1], ADAaverage, ADAmax, 100*(ADAcloses[len(Date)-1]-ADAcloses[0])/ADAcloses[0], 100*(ADAcloses[len(Date)-1]-ADAvalue6months)/ADAvalue6months]
                }
        display(pd.DataFrame(ADAtable))

# if XRP is requested

    else:
        
        # Read the files
        
        XRPread = pd.read_excel (r'C:\Users\Doğan\Desktop\Doğan\Crypto_World\XRP-USD.xlsx')
        XRPcloses=XRPread['Adj Close']        
        
        # Plot the historical data
        
        fig, ax = plt.subplots(figsize=(19, 5))
        fig.subplots_adjust(bottom=0.15, left=0.2)
        ax.plot(Date, XRPcloses)
        ax.set_xlabel('Date [in weeks]',size=15)
        ax.set_ylabel('XRP Values ($)',size=15)
        ax.set_title('Weekly XRP-USD Graph for last 3 years', size=15, fontweight='bold')
        plt.show()
        
        # Give some hints to the user
        
        XRPaverage = np.average(XRPcloses)
        XRPmax = max(XRPcloses)
        XRPvalue6months=XRPcloses[len(Date)-23]
        XRPtable={'Statistics' : ['The Last Week Close', 'Average($)', 'ATH($)', 'Increase in last 3 years(%)', 'Increase in last 6 months(%)'],
                'Values' : [XRPcloses[len(Date)-1], XRPaverage, XRPmax, 100*(XRPcloses[len(Date)-1]-XRPcloses[0])/XRPcloses[0], 100*(XRPcloses[len(Date)-1]-XRPvalue6months)/XRPvalue6months]
                }
        display(pd.DataFrame(XRPtable))
