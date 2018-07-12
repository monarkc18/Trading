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

def Data_Frame_plot(Data_Frame):
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

#---------------------------------------TRADING ALGORITHM 1------------------------------------------------------------------------
    i=0
    Buy_list=[]
    Sell_list=[]
    Dates_Sell =[]
    Dates_Buy=[]

    for i in range(0,801):
        if MVA_10_series_adj[i] > MVA_50_series_adj[i] > MVA_120_series_adj[i] > MVA_200_series[i] :

            print(Dates_series[i])
            print(Value_Original_adj[i])
            print('Buy')
            Buy_list.append(Value_Original_adj[i])
            Dates_Buy.append(Dates_series[i])
            i += 1

        elif MVA_10_series_adj[i] > MVA_50_series_adj[i] > MVA_120_series_adj[i] < MVA_200_series[i] :

            print(Dates_series[i])
            print(Value_Original_adj[i])
            #print('Buy POTENTIAL')
            i += 1

        elif MVA_10_series_adj[i] > MVA_50_series_adj[i] < MVA_120_series_adj[i] < MVA_200_series[i]:

            print(Dates_series[i])
            print(Value_Original_adj[i])
           # print('Buy POTENTIAL -1')
            i += 1

        elif MVA_10_series_adj[i] > MVA_50_series_adj[i] < MVA_120_series_adj[i] < MVA_200_series[i]:

            print(Dates_series[i])
            print(Value_Original_adj[i])
            print('Buy POTENTIAL -2')
            i += 1

        elif MVA_10_series_adj[i] < MVA_50_series_adj[i] < MVA_120_series_adj[i] < MVA_200_series[i]:

            print(Dates_series[i])
            print(Value_Original_adj[i])
           # print('Buy POTENTIAL -3')
            i += 1

        elif  MVA_50_series_adj[i] < MVA_200_series[i]:

            print(Dates_series[i])
            print(Value_Original_adj[i])
            print('Sell')
            Sell_list.append(Value_Original_adj[i])
            Dates_Sell.append(Dates_series[i])
            i += 1




    Buy_list = pd.Series(Buy_list)
    Dates_Buy = pd.Series(Dates_Buy)
    Sell_list = pd.Series(Sell_list)
    Dates_Sell=pd.Series(Dates_Sell)

    print(Buy_list)
    print(Dates_Buy)
    print(Sell_list)
    print(Dates_Sell)



    DF_Buy = pd.DataFrame({'Date':Dates_Buy,'Buy_Price':Buy_list})
    DF_Buy = DF_Buy.set_index('Date')

    DF_Sell = pd.DataFrame({'Date': Dates_Sell, 'Sell_Price': Sell_list})
    DF_Sell = DF_Sell.set_index('Date')



    print(DF_Buy)
    print(DF_Sell)

    Data_Frame_plot(Data_Frame_adj_Dates)#------------------------Plotting Function is called
    Data_Frame_plot(DF_Buy)
    Data_Frame_plot(DF_Sell)

    print(len(Buy_list))
    print(len(Dates_Buy))
    print(len(Sell_list))
    print(len(Dates_Sell))






#----------------------------------------------------------------------------------------------------------------------------------
MVA_DF("BOE-XUDLJYD.csv")#-------------------------------------Calls MVA FUNCTION to plot respective Currec






















