import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import statistics as st
import datetime as dt
from datetime import date
import seaborn as sns
import numpy as np
import plotly.express as px
from tkinter import *


# to extract this year recommendation from the banks to buy stocks
year = dt.datetime.now().year
today = date.today()
first = dt.datetime(day=1,month=1,year=year)
first = first.strftime('%Y-%m-%d')


# note add the ratios from previous years


#timing the excution when the program started
begin_time = dt.datetime.now()

# the history for the favourite stocks
# Apple = None
# Microsoft = None
# Amazon = None
# Tesla = None
# Nvida = None
# JP_Morgan = None
# FaceBook = None
# Citi_bank = None
# Barclays = None
# Google = None
# Netflix = None
# incase someone wants other companies it will be saved in this list
others = []
# saving the maximum history to see who performed the best in terms of the whole history
max_percent = {}
# maximum during the custom period
custom_percent = {}

# make sure the number of stocks in stock's list is an odd number for a better analysis i.e the median function otherwise it will give an error
stocks = ["AAPL", "MSFT", "AMZN", "TSLA", "NVDA", "FB", "GOOG", "JPM", "NFLX","BA","NKE","WMT","V","PYPL","BAC"]
for s in stocks:
    ticker = yf.Ticker(s)
    # for a certain time of period use download instead of history
    #hist = yf.download(s, start="2020-01-01", end="2021-01-01")
    hist = ticker.history(period="max")
    print(s)
    #print(ticker.sustainability)
    reco = ticker.recommendations
    recom = reco.loc[first:today]
    print(recom.to_string())
    print(hist["Close"].describe())
    # print the last cell in order the price for today
    print(hist["Close"].tail(1))
    # deleting dividends and splits as there will be a separate analysis
    # or use
    #df = df.drop('column_name', 1)
    del hist["Dividends"]
    del hist["Stock Splits"]
    # percentage change in closing price
    percentage = pd.Series(hist["Close"])
    percentage = percentage.pct_change() * 100
    #print(percentage)
    # i want to see how much the stock changed since the ipo until to this day
    total_sum = 0
    num = 100000
    v = 0
    for GG in percentage:
        if GG < num:
            total_sum= total_sum + GG

    print("The total percentage change for the whole history " + s + ": " + str(int(total_sum)) + "%")
    max_percent[s] = int(total_sum)
    # custom date for the percentage for a certain period
    custom_date = percentage.loc[dt.date(year=2008, month=10, day=1):today]
    custom_date_sum = 0
    for B in custom_date:
        if B < num:
            custom_date_sum = custom_date_sum + B
    custom_percent[s] = int(custom_date_sum)
    print(" the custom date percentage change " + s + ": " + str(int(custom_date_sum)) + "%")
    # finding the difference
    difference = total_sum - custom_date_sum
    print("  the difference between the whole history and the custome date for " + s+ ": " + str(int(difference)) + "%")
    print("*" * 84)
    # change the currency to the local currency 01/2021 rate
    hist["Closing in KD"] = hist["Close"] * 0.3
    # adding it to the table
    hist["percentage change in the closing "] = percentage
    #print(hist.to_string())
    # attributes = ["High", "Close", "Low"]
    # hist["Close"].plot()
    # plt.title(s)
    # plt.legend()
    # plt.show()
    # hist["percentage change in the closing "].plot()
    # plt.title(s)
    # plt.show()
    # if s == "AAPL":
    #     Apple = hist
    # elif s == "MSFT":
    #     Microsoft = hist
    # elif s == "TSLA":
    #     Tesla = hist
    # elif s == "AMZN":
    #     Amazon = hist
    # elif s == "NVDA":
    #     Nvida = hist
    # elif s == "JPM":
    #     JP_Morgan = hist
    # elif s == "FB":
    #     FaceBook = hist
    # elif s == "GOOG":
    #     Google = hist
    # elif s == "C":
    #     Citi_bank = hist
    # elif s == "BCS":
    #     Barclays = hist
    # elif s == "NFLX":
    #     Netflix = hist
    # else:
    #     others.append(hist)




# alternative plotting for plotly
# plt.plot(Apple["Close"], label="Apple")
# plt.plot(Microsoft["Close"], label="Microsoft")
# plt.plot(Tesla["Close"], label="Tesla")
# plt.plot(Amazon["Close"], label="amazon")
# plt.plot(Nvida["Close"], label="nvida")
# plt.plot(JP_Morgan["Close"], label="J.P Morgan ")
# plt.plot(FaceBook["Close"], label="Facebook")
# plt.plot(Google["Close"], label="Google")
# plt.plot(Citi_bank["Close"], label="Citi bank")
# plt.plot(Barclays["Close"], label="barclays")
# plt.plot(Netflix["Close"], label="netflix")
# plt.legend()
# plt.show()




# this function for the median it takes the value of the median and tries to locate its key
def get_key(dictionary,value):
    for k in dictionary.keys():
        if value == dictionary[k]:
            return k



#name of the higest price to book ratio
max_history = max(max_percent, key=max_percent.get)
#to get the actual number
max_hist = max(max_percent.values())
# getting the mid value
mid_hist = st.median(max_percent.values())
min_history = min(max_percent, key=max_percent.get)
# getting the min value
min_hist = min(max_percent.values())
print("best performed stock according to percentage change: ")
print("highest percentage change : " + max_history + ": "+str(max_hist) + "%")
print("The middle of the list: " + get_key(max_percent, mid_hist) + ": " + str(mid_hist)+ "%")
print("minimum percentage change: " + min_history + ": " + str(min_hist) + "%")
print("*" * 44)


# this is for the custom period
max_custom = max(custom_percent, key=custom_percent.get)
max_cus = max(custom_percent.values())
mid_custom = st.median(custom_percent.values())
min_custom = min(custom_percent, key=max_percent.get)
min_cust = min(custom_percent.values())
print("best performed custom date stock according to percentage change: ")
print("highest percentage change for custom date : " + max_custom + ": "+str(max_cus) + "%")
print("The middle of the list: " + get_key(custom_percent, mid_custom) + ": " + str(mid_custom)+ "%")
print("minimum percentage change for custom date: " + min_custom + ": " + str(min_cust) + "%")
print("*" * 44)


# tracking index funds
Dow_Jones30 = None
S_P500 = None
FTSE100 = None
DAX = None


index_funds = ["BTC-USD","GC=F"]
for i in index_funds:
    ticker2 = yf.Ticker(i)
    hist1 = ticker2.history(period="max")
    # hist1["Close"].plot()
    # plt.title(i)
    # plt.show()
    if i == "^DJI":
        Dow_Jones30 = hist1
    elif i == "^GSPC":
        S_P500 = hist1
    elif i == "^FTSE":
        FTSE100 = hist1
    else:
        DAX = hist1
# plt.plot(Dow_Jones30["Close"], label="Dow jones")
# plt.plot(FTSE100["Close"], label="FTSE")
# plt.plot(S_P500["Close"], label="S_P500")
# plt.plot(DAX["Close"], label="Dax")
# plt.legend()
# plt.show()

# adding my stocks with the benchmark fund in order to find the correlation
list = index_funds + stocks
# correlation for the stocks
#getting only the close price for the company
data = yf.download(list, start= "1980-12-12")["Close"]
# plotting the varibales
plot= px.line(data_frame=data)
plot.show()
# doing correlation
data = data.fillna(method="ffill")
corr = data.corr()
# to delete the upper tringle of the correlation table
mask = np.triu(np.ones_like(corr))
sns.heatmap(corr,annot=True, mask=mask)
plt.tight_layout()
plt.show()



#financial statements for latest quarter
#since the financials function is not working in yfinance library, i have used pandas to extract the information
apple = []
microsoft = []
amazon = []
tesla = []
nvida = []
jp_Morgan = []
facebook = []
citi_bank = []
barclays = []
google = []
netflix = []
Other = []
for E in stocks:
    statistics = pd.read_html(f'https://finance.yahoo.com/quote/{E}/key-statistics?p={E}')
    financials = statistics[7:]
    if E == "AAPL":
        apple.append(financials)
    elif E == "MSFT":
        microsoft.append(financials)
    elif E == "TSLA":
        tesla.append(financials)
    elif E== "AMZN":
        amazon.append(financials) 
    elif E == "NVDA":
        nvida.append(financials) 
    elif E == "JPM":
        jp_Morgan.append(financials) 
    elif E == "FB":
        facebook.append(financials) 
    elif E == "GOOG":
        google.append(financials) 
    elif E == "C":
        citi_bank.append(financials)
    elif E == "BCS":
        barclays.append(financials) 
    elif E == "NFLX":
        netflix.append(financials)
    else:
       Other.append(financials)


# list to print the whole statments
fin_state = [apple,microsoft,amazon,tesla,nvida,facebook,google,jp_Morgan,citi_bank,barclays,netflix,Other]
stocks1 = stocks

for pop in fin_state:
    # to print the name of the variable
    for lj in stocks1:
        print(lj)
        # then removing it for the list in order for the loop to break and start with new variable
        stocks1.remove(lj)
        # then breaking the loop to print the statement of the company
        break
    print(pop)
    print("*"*84)

#fundemental analysis and important information that is important to know
stock_beta_temp = {}
stock_beta = {}
price_to_book_temp = {}
price_to_book = {}
forward_pe_temp = {}
forward_pe = {}
book_value_temp = {}
book_value = {}
EPS = {}
Eps = {}
profit_margin_temp = {}
profit_margin = {}
for c in stocks:
    # you could use rather than a for loop a named tuple of Ticker objects, however i used dictionary for a btter underestanding
    #^ tickers = yf.Tickers("msft aapl goog")
    ticker3 = yf.Ticker(c)
    # to access each ticker use
    # tickers.tickers.MSFT.info
    # tickers.tickers.AAPL.history(period="1mo")
    # tickers.tickers.GOOG.actions
    #for a general info use (ticker.info) only then u could specify which ratios u want for ur investment
    #^ print(msft.info)
    stock_beta_temp[c] = ticker3.info["beta"]
    price_to_book_temp[c] = ticker3.info["priceToBook"]
    forward_pe_temp[c] = ticker3.info["forwardPE"]
    book_value_temp[c] = ticker3.info["bookValue"]
    EPS[c]= ticker3.info["forwardEps"]
    profit_margin_temp[c] = ticker3.info["profitMargins"]


# ba company has an empty item in price book ratio so i had to remove it and add a fake item to fix the median function
# created a function for the future just in case it there will be any none in the ratios
def for_error_ratios(dict):
    for L,p in dict.items():
        if dict == price_to_book_temp:
            if dict[L] != None:
                price_to_book[L] = price_to_book_temp[L]
            else:
                price_to_book["an empty item just for median function for the company " + L] = 0.5
        elif dict == stock_beta_temp:
            if dict[L] != None:
                stock_beta[L] = stock_beta_temp[L]
            else:
                stock_beta["an empty item just for median function for the company " + L] = 0.5
        elif dict == forward_pe_temp:
            if dict[L] != None:
                forward_pe[L] = forward_pe_temp[L]
            else:
                forward_pe["an empty item just for median function for the company " + L] = 0.5
        elif dict == book_value_temp:
            if dict[L] != None:
                book_value[L] = book_value_temp[L]
            else:
                book_value["an empty item just for median function for the company " + L] = 0.5
        elif dict == EPS:
            if dict[L] != None:
                Eps[L] = EPS[L]
            else:
                Eps["an empty item just for median function for the company " + L] = 3
        elif dict == profit_margin_temp:
            if dict[L] != None:
                profit_margin[L] = profit_margin_temp[L]
            else:
                profit_margin["an empty item just for median function for the company " + L] = 0.1111

for_error_ratios(price_to_book_temp)
for_error_ratios(stock_beta_temp)
for_error_ratios(forward_pe_temp)
for_error_ratios(book_value_temp)
for_error_ratios(EPS)
for_error_ratios(profit_margin_temp)




# print(stock_beta)
# print(price_to_book)
# print(forward_pe)
# print(book_value)
# print(Eps)
# print(profit_margin)


comparing_beta = max(stock_beta, key= stock_beta.get)
beta_max = max(stock_beta.values())
beta_min = min(stock_beta, key=stock_beta.get)
min_beta = min(stock_beta.values())
mid = st.median(stock_beta.values())
print("Beta: a measure of the volatility or systematic risk \n""if Bete > 1 theoretically more volatile than the market \n" "if Beta < 1 then less volatile than the market \n""if Beta = 1 it means strongly correlated to the market")
print("highest Beta: " + comparing_beta + ": "+str(beta_max))
print("The middle Beta: " + get_key(stock_beta, mid) + ": " + str(mid))
print("minimum Beta: " + beta_min + ": " + str(min_beta))
print("*" * 44)

name_key = max(price_to_book, key=price_to_book.get)
max_value = max(price_to_book.values())
mid1 = st.median(price_to_book.values())
min_p = min(price_to_book, key=price_to_book.get)
min_price = min(price_to_book.values())
print("P/B: measures the market's valuation of a company relative to its book value \n""Traditionally, any value under 1.0 is considered a good P/B for value investors, indicating undervalued or something fundamentally wrong with the company.")
print("highest P/B : " + name_key + ": "+str(max_value))
print("The middle P/B: " + get_key(price_to_book, mid1) + ": " + str(mid1))
print("minimum P/B: " + min_p + ": " + str(min_price))
print("*" * 44)

pe_value = max(forward_pe, key=forward_pe.get)
pe_max = max(forward_pe.values())
mid2 = st.median(forward_pe.values())
min_pe = min(forward_pe, key=forward_pe.get)
pe_min = min(forward_pe.values())
print("P/E: whether a company's stock price is overvalued or undervalued ")
print("highest P/E: " + pe_value + ": "+str(pe_max))
print("The middle P/E: " + get_key(forward_pe, mid2) + ": " + str(mid2))
print("minimum P/E: " + min_pe + ": " + str(pe_min))
print("*" * 44)

book = max(book_value, key=book_value.get)
book_max = max(book_value.values())
mid3 = st.median(book_value.values())
min_book = min(book_value, key=book_value.get)
book_min = min(book_value.values())
print("Book Value per share :  metric can be used by investors to gauge whether a stock price is undervalued \n"" a company’s BVPS is higher than its market value per share—its current stock price—then the stock is considered undervalued.")
print("highest Book Value per share: " + book + ": "+str(book_max))
print("The middle Book Value per share: " + get_key(book_value, mid3) + ": " + str(mid3))
print("minimum Book Value per share: " + min_book + ": " + str(book_min))
print("*" * 44)

eps = max(Eps,  key= Eps.get)
eps_max = max(Eps.values())
mid4 = st.median(Eps.values())
min_eps = min(Eps, key=Eps.get)
eps_min = min(Eps.values())
print("EPS: tells you how well a company is generating profit for its shareholders")
print("highest EPS: " + eps + ": "+str(eps_max))
print("The middle EPS: " + get_key(Eps, mid4) + ": " + str(mid4))
print("minimum EPS: " + min_eps + ": " + str(eps_min))
print("*" * 44)

profit = max(profit_margin, key=profit_margin.get)
profit_max = max(profit_margin.values())
mid5 = st.median(profit_margin.values())
min_profit = min(profit_margin, key=profit_margin.get)
profit_min = min(profit_margin.values())
print("Profit Margin:  indicates how many cents of profit has been generated for each dollar of sale ")
print("highest Profit Margin: " + profit + ": "+str(profit_max))
print("The middle Profit Margin: " + get_key(profit_margin, mid5) + ": " + str(mid5))
print("minimum Profit Margin: " + min_profit + ": " + str(profit_min))
print("*" * 44)

hold ={}

# actions(splits in the stocks and dividends) also the major holdings in the company
# ^ or # print(msft.dividends) print(msft.splits)
for Q in stocks:
    ticker4 = yf.Ticker(Q)
    print(Q.upper())
    df = ticker4.splits
    # removing the the dated where stock splits didn't happen
    stock_split = df != 0.0
    stock_split = df.loc[stock_split]
    df1 = ticker4.dividends
    # removing the the dated where dividends didn't happen
    dividend = df1 != 0.0
    dividend = df1.loc[dividend]
    # looking at the percentage increase in dividends using pandas
    change = pd.Series(dividend)
    change = change.pct_change() * 100
    change_sum = 0
    for O in change:
        if O < num:
            change_sum = change_sum + O
    print("The total percentage change for the whole history in divided for " + Q + ": " + str(int(change_sum)) + "%")
    # creating a table
    table = pd.DataFrame()
    # adding a column to the empty table
    table["dividend"] = dividend
    table["change"] = change
    print(stock_split)
    # print(table.to_string())
    holders = ticker4.institutional_holders.to_string()
    hold[Q] = holders
    print(holders)
    print("*" * 84)
    # some companies doesn't issue dividends so it has been exluded for faster excution time i.e amazon
    if int(change_sum) != 0:
        plt.plot(table["dividend"], label= Q)
        plt.title("Dividend for " + Q)
        plt.show()
        plt.plot(table["change"], label= Q)
        plt.title("Dividend percentage change " + Q)
        plt.show()
    else:
        continue

# the clock now after finishing the program
end_time = dt.datetime.now()
# taking the difference to figure how much time did the program take to execute the whole program
print("The structure for the execution time as follows: ""hour:minute:second:microsecond")
print(end_time - begin_time)

#Gui
# main window
window = Tk()
window.title("Stock app research")
window.configure(background="black")

#Stock name label
Label(window, text="Enter a stock name you want to know about: ", bg= "black", fg= "white", font="none 12 bold").grid(row=1, column= 0, sticky=W)

# key function
def click():
    entered_text= text_entry.get() # this to collect the text from the text box
    # deleting the output from the text in order the new stock comes in
    output.delete(0.0,END)
    output3.delete(0.0,END)
    dict1 = ["Eps: ","profit_margin: ","stock_beta: ","price_to_book: ","book_value: ","forward_pe: "]
    dict2 = [Eps,profit_margin,stock_beta,price_to_book,book_value,forward_pe]
    for LL in dict2:
        try:
            definition = LL[entered_text]
        except:
            definition = "Sorry the stock does not exists at the moment"
        po = "N/A"
        for lo in dict1:
            if lo == "Eps: ":
                po= lo
                #inserting in the box where the anchor is
                output.insert(INSERT, po)
                output.insert(INSERT, definition)
                # after inserting it we are saying make a new line in the box
                output.insert(END, "\n")
                dict1.remove("Eps: ")
                break
            elif lo == "profit_margin: ":
                po = lo
                output.insert(INSERT, po)
                output.insert(INSERT, definition)
                output.insert(END, "\n")
                dict1.remove("profit_margin: ")
                break
            elif lo == "stock_beta: ":
                po= lo
                output.insert(INSERT, po)
                output.insert(INSERT, definition)
                output.insert(END, "\n")
                dict1.remove("stock_beta: ")
                break
            elif lo == "price_to_book: ":
                po=lo
                output.insert(INSERT, po)
                output.insert(INSERT, definition)
                output.insert(END, "\n")
                dict1.remove("price_to_book: ")
                break
            elif lo =="book_value: ":
                po=lo
                output.insert(INSERT, po)
                output.insert(INSERT, definition)
                output.insert(END, "\n")
                dict1.remove("book_value: ")
                break
            elif lo == "forward_pe: ":
                po=lo
                output.insert(INSERT, po)
                output.insert(INSERT, definition)
                output.insert(END, "\n")
                dict1.remove("forward_pe: ")
    try:
        holds = hold[entered_text]
    except:
        holds = "Sorry the stock does not exists at the moment"
    output3.insert(INSERT,holds)



# text entry box
text_entry = Entry(window, width=60, bg="white")
text_entry.grid(row=2, column=0, sticky=W)
text_entry.insert(INSERT, "Enter the Ticker for your particular Stock: ")

# add a button
Button(window, text="Search", width= 6, command= click).grid(row=3, column = 0, sticky = W)

# another label
Label(window, text="Statistics for the Stock", bg= "black", fg= "white", font="none 12 bold").grid(row=4, column= 0, sticky= W)

# output box
output = Text(window, width= 75, height = 6, background= "white")
output.grid(row=5, column=0 , columnspan= 2, sticky= W)

# adding a scrolling bar
sv2= Scrollbar(window)
sv2.grid(row=5, column =2, sticky=W)

# configuration the scroll bar with the text box
output.configure(yscrollcommand= sv2.set)
sv2.configure(command= output.yview)

# another output box for the included stocks
output1= Text(window,width= 40, height = 6, background= "white")
output1.grid(row=10, column=2, sticky=W)
output1.insert(INSERT, "The companies that is in included:\n ")
output1.insert(INSERT, "Apple = AAPL \n")
output1.insert(INSERT, "Tesla = TSLA \n")
output1.insert(INSERT, "Amazon = AMZN \n")
output1.insert(INSERT, "FaceBook = FB \n")
output1.insert(INSERT, "Barclays = BCS \n")
output1.insert(INSERT, "Pfizer = PFE \n")
output1.insert(INSERT, "Jp Morgan = JPM \n")
output1.insert(INSERT, "Boeing = BA \n")
output1.insert(INSERT, "Google = GOOG \n")
output1.insert(INSERT, "Netflix = NFLX \n")
output1.insert(INSERT, "Nvida = NVDA \n")
output1.insert(INSERT, "Citi Bank = C \n")
output1.insert(INSERT, "Microsoft = MSFT \n")

# adding a scrolling bar
sv1= Scrollbar(window)
sv1.grid(row=10, column =3, sticky=W)

# configuration the scroll bar with the text box
output1.configure(yscrollcommand= sv1.set)
sv1.configure(command= output1.yview)

# label
Label(window, text="The biggest holder for this stock", bg= "black", fg= "white", font="none 12 bold").grid(row=8, column=0, sticky= W)

# i need to get the holdernames
output3= Text(window,width= 100, height =10, background= "white")
output3.grid(row=9, column=0, sticky=W)


# exit function
def close_window():
    window.destroy()
    exit()

#exit button
Button(window, text="Exit", width= 4, command= close_window).grid(row=6, column = 0, sticky = W)

#run the main loop
window.mainloop()
