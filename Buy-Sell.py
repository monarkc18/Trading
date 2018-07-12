'''
DATE SERIES ADJUSTED PLOTTED GRAPH Moving Average adjusted
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime
#import seaborn


def simple_mva(value, mvarange):
    weights = np.repeat(1.0, mvarange) / mvarange
    simple_mva = np.convolve(value, weights, 'valid')
    return simple_mva

def plot_with_mva(Data_Frame):
    Data_Frame.plot()
    plt.show()

#def Buy_signal():

#def Buy(Current,MVA_,MVA_L)

def MVA_DF(File):
    Data_File = pd.read_csv(File)

    D_F_Data_COL = Data_File.loc[0:1000,'Value']
    D_F_Date_COL = Data_File.loc[0:1000,'Date']

    Value_Original = D_F_Data_COL.tolist()#-------------------Parsing Data from CSV DATA_Frame to a lis t
    Value_Original = Value_Original[::-1]

    Value_Original_adj = Value_Original[199:1001]
    Value_Original_adj = pd.Series(Value_Original_adj)
    Value_series   =  pd.Series(Value_Original)#--------------Parsing Values from list to a pandas Series Object

    Dates_Original = D_F_Date_COL.tolist() #-------------------Parsing Dates from CSV DATA_Frame to a list
    Dates_series = pd.Series(Dates_Original[801::-1])#------------------Parsing Dates to a Pandas Series Object

    MVA_10_Val = simple_mva(Value_Original,10)#------------------Parsing output of Simple moving average to a list
    MVA_50_Val = simple_mva(Value_Original,50)#------------------Parsing output of Simple moving average to a list
    MVA_120_Val = simple_mva(Value_Original,120)#------------------Parsing output of Simple moving average to a list
    MVA_200_Val = simple_mva(Value_Original,200)#------------------Parsing output of Simple moving average to a list


    MVA_10_series_adj = pd.Series(MVA_10_Val[190:])#------------------Parsing Simple moving average  list to a Pandas Series Object
    MVA_50_series_adj = pd.Series(MVA_50_Val[150:])#------------------Parsing Simple moving average  list to a Pandas Series Object
    MVA_120_series_adj = pd.Series(MVA_120_Val[80:])#------------------Parsing Simple moving average  list to a Pandas Series Object
    MVA_200_series = pd.Series(MVA_200_Val)#------------------Parsing Simple moving average  list to a Pandas Series Object

#----------------------------------------------Creating DataFrame--------------------------------------------------

    Data_Frame_adj = pd.DataFrame({'Dates':Dates_series,'MVA_10':MVA_10_series_adj,'MVA_50':MVA_50_series_adj,'MVA_120':MVA_120_series_adj,'MVA_200':MVA_200_series,'Data':Value_Original_adj})
    Data_Frame_adj["Dates"] = pd.to_datetime(Data_Frame_adj["Dates"])#--------------------Parsing the old Data Frame to Date time series representation....
    Data_Frame_adj_Dates = Data_Frame_adj.set_index('Dates')
    print(Data_Frame_adj_Dates)
    plot_with_mva(Data_Frame_adj_Dates)  # ------------------------Plotting Function is called

    MVA_DF("BOE-XUDLJYD.csv")  # -------------------------------------Calls MVA FUNCTION to plot respective Currec

    #---------------------------------------TRADING ALGORITHM 1------------------------------------------------------------------------
i=0

for num in range(0,801):
       print('Buy')
       i += 1
























