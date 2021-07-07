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
        Date=ETHread['Date']

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

# if LTC is requested

    elif selection=='LTC':  
        
        # Read the files
        
        LTCread = pd.read_excel (r'C:\Users\Doğan\Desktop\Doğan\Crypto_World\LTC-USD.xlsx')
        LTCcloses=LTCread['Adj Close']
        Date=LTCread['Date']

        # Plot the historical data

        fig, ax = plt.subplots(figsize=(19, 5))
        fig.subplots_adjust(bottom=0.15, left=0.2)
        ax.plot(Date, LTCcloses)
        ax.set_xlabel('Date [in weeks]',size=15)
        ax.set_ylabel('LTC Values ($)',size=15)
        ax.set_title('Weekly LTC-USD Graph for last 3 years', size=15, fontweight='bold')
        plt.show()

        # Give some hints to the user
        
        LTCaverage = np.average(LTCcloses)
        LTCmax = max(LTCcloses)
        LTCvalue6months=LTCcloses[len(Date)-23]
        LTCtable={'Statistics' : ['The Last Week Close', 'Average($)', 'ATH($)', 'Increase in last 3 years(%)', 'Increase in last 6 months(%)'],
                'Values' : [LTCcloses[len(Date)-1], LTCaverage, LTCmax, 100*(LTCcloses[len(Date)-1]-LTCcloses[0])/LTCcloses[0], 100*(LTCcloses[len(Date)-1]-LTCvalue6months)/LTCvalue6months]
                }
        display(pd.DataFrame(LTCtable))

# if BCH is requested

    elif selection=='BCH':
        
        # Read the files
        
        BCHread = pd.read_excel (r'C:\Users\Doğan\Desktop\Doğan\Crypto_World\BCH-USD.xlsx')
        BCHcloses=BCHread['Adj Close']
        Date=BCHread['Date']
              
        # Plot the historical data
        
        fig, ax = plt.subplots(figsize=(19, 5))
        fig.subplots_adjust(bottom=0.15, left=0.2)
        ax.plot(Date, BCHcloses)
        ax.set_xlabel('Date [in weeks]',size=15)
        ax.set_ylabel('BCH Values ($)',size=15)
        ax.set_title('Weekly BCH-USD Graph for last 3 years', size=15, fontweight='bold')
        plt.show()
        
        # Give some hints to the user
        
        BCHaverage = np.average(BCHcloses)
        BCHmax = max(BCHcloses)
        BCHvalue6months=BCHcloses[len(Date)-23]
        BCHtable={'Statistics' : ['The Last Week Close', 'Average($)', 'ATH($)', 'Increase in last 3 years(%)', 'Increase in last 6 months(%)'],
                'Values' : [BCHcloses[len(Date)-1], BCHaverage, BCHmax, 100*(BCHcloses[len(Date)-1]-BCHcloses[0])/BCHcloses[0], 100*(BCHcloses[len(Date)-1]-BCHvalue6months)/BCHvalue6months]
                }
        display(pd.DataFrame(BCHtable))

# if XRP is requested

    else:
        
        # Read the files
        
        XRPread = pd.read_excel (r'C:\Users\Doğan\Desktop\Doğan\Crypto_World\XRP-USD.xlsx')
        XRPcloses=XRPread['Adj Close']   
        Date=XRPread['Date']
        
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
