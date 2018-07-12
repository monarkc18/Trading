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

#--------------------------------TRADING ALGORITHM LOGIC ENDDS


    Buy_list = pd.Series(Buy_list[0:57])
    Dates_Buy = pd.Series(Dates_Buy[0:57])
    Sell_list = pd.Series(Sell_list)
    Dates_Sell=pd.Series(Dates_Sell)


    Buy_list_list = Buy_list.tolist()
    Sell_list_list = Sell_list.tolist()


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

#    Data_Frame_WO_MVA =


    frames = [DF_Buy,DF_Sell]
    result = pd.concat(frames)
    print(result)


#--------------------------------------------------INTEGRATING PROFIT LOSS-------------------------

    trade_cost_buy = []  # List for storing the value of trading cost of buy
    update_list_amount = []  # List for storing the value of available balance
    trade_cost_sell = []  # List for storing the value of trading cost of sell
    # update_list_sell=[]
    final_amount_list = []  # List for storing the value of final amount
    final_profit_loss = []  # List for storing the value of final profit or loss
    flag = False

    quant = 200

    def buy(i, j):  # Funcation for buy

        k = 0
        a = 0

        print("Please enter your balance:\n")
        amount = input()  # getting the value in string
        amount = float(amount)  # convert sting into integer value

        for value in Buy_list_list:
            total_trade = Buy_list_list[k] * quant  # total trade for buy
            print("\nBuy", k, ":", total_trade)
            trade_cost_buy.append(total_trade)  # update the list

            if (total_trade != 0):
                flag = True
            k = k + 1  # increment

        for update in trade_cost_buy:
            avl_balance = amount - trade_cost_buy[a]
            amount = avl_balance
            # amount=avl_balance
            print("\nBalance", a, "is:", avl_balance)
            a = a + 1
            if avl_balance < 0:
                print("Margin")
                update_list_amount.append(avl_balance)  # update the list

            elif avl_balance > 0:
                print("No Margin")
                update_list_amount.append(avl_balance)  # update the list

               # Total_margin = update_list_amount(update_list_amount.__len__() -1 )


    buy(10, 20)  # Function call to buy

    print("\n..........Your selling value..........")

    def sell(p, q):  # Funcation for sell

        b = 0

        for value1 in Sell_list_list:

            if (flag == True):  # checking the condition if buy is done or not
                print("Sorry,Sell is not possible yet!\n")

            else:
                total_trade1 = Sell_list_list[b] * quant  # total trade for sell
                print("\nSell", b, "is:", total_trade1)
                trade_cost_sell.append(total_trade1)  # update the list
                b = b + 1  # increment

    sell(14, 25)  # function call to sell

    print("\n..........Your Final Amount..........")

    def final(a, b):  # Funcation for  profit

        y = 0
        z = 0
        m = 0
        p = 0

        for calculate in trade_cost_sell:
            for calculate1 in trade_cost_buy:

                final_amount = (trade_cost_sell[y] - trade_cost_buy[z])  # Final amount(profit or Loss)

                final_amount_list.append(final_amount)  # update the list
                y = y + 1
                z = z + 1
                p = p + 1

                if (final_amount_list[m] < 0):
                    print("\nYou get", final_amount, "  in forex treding ", m)
                    m = m + 1  # increment

                elif (final_amount_list[m] > 0):
                    print("\nYou get", final_amount, "  in forex trading ", m)
                    m = m + 1  # increment

                else:
                    print("\nSorry!your final amount is zero!")

                    m = m + 1  # increment

            return




    final(14, 17)  # function call to profit

    print("\n.......... Your profit or Loss ..........")

    def profit(i):  # Function define for profit
        a = 0
        sum = 0
        for pro_or_loss in final_amount_list:  # logic for getting the value from list
            sum1 = sum + final_amount_list[a]
            sum = sum1
            a = a + 1
            final_profit_loss.append(sum1)  # List is updated

        if sum > 0:
            print("\nYour Profit is:", sum)
            if (update_list_amount[len(update_list_amount)- 1] < 0):
                #print("No Margin is:", abs(update_list_amount[len(update_list_amount)- 1]))
                print(print("Margin is:", abs(update_list_amount[len(update_list_amount)- 1])))
            else:
                print("You have No Margin Your Balance is:   ",abs(update_list_amount[len(update_list_amount)- 1]))
        elif sum < 0:
            print("\nYour Loss is:", sum)
           # print("Margin is:", update_list_amount[len(update_list_amount) - 1])

    profit(10)
    #list_len1=len(update_list_amount)-1


#---------------------------------------------------PROFIT LOSS END--------------------------------------------------


#----------------------------------------------------------------------------------------------------------------------------------
MVA_DF("BOE-EUR-USD.csv")#-------------------------------------Calls MVA FUNCTION to plot respective Currec























