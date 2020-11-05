import pandas as pd
import statistics as stat
from yahooquery import *

# Ticker input here
#stock_list = [line.rstrip('\n') for line in open("DAX.txt", "r")]

#for stock in stock list:
tickers = Ticker('LOGN.SW')
bs = tickers.balance_sheet()
inst = tickers.income_statement()
cash = tickers.cash_flow()

# Summary statistics

summary = tickers.summary_detail
summary = pd.DataFrame.from_dict(summary, orient='index')

#cap = summary['marketCap']
#print('marketcap: ' + cap.to_string())

div = summary['dividendRate']
print('dividend: ' + div.to_string())

div_yield = summary['dividendYield'] *100
print('yield: ' + div_yield.to_string() + ' %')

div_date = summary['exDividendDate']
print('ex-dividend date: ' + div_date.to_string())

payout_ratio = summary['payoutRatio'] *100
payout_ratio = round(payout_ratio,2)
print('payout ratio: ' + payout_ratio.to_string() + ' %')

pe = summary['forwardPE']
pe = round(pe,2)
print('Forward P/E: ' + pe.to_string())

#print(tickers._get_historical_data())

# Get balance sheet
#for stock in stock_list
    #try:
        #stock_bs = bs.loc[stock]
        #stock_inst = inst.loc[stock]
    #bs = tickers.balance_sheet()
    #bs = pd.DataFrame(bs)
    #bs = bs.set_index('endDate')
    #print(bs)


## Balance sheet variables to extract ##

# Total Assets
total_assets = bs['totalAssets']
avg_total_assets = stat.mean(total_assets)

# Total Current Liabilities
total_current_liabilities = bs['totalCurrentLiabilities']
avg_total_current_liabilities = stat.mean(total_current_liabilities)

# Total Liabilities
total_liabilities = bs['totalLiab']
avg_total_liabilities = stat.mean(total_liabilities)

## Get income statement ##
    #inst = tickers.income_statement()
    #inst = pd.DataFrame(inst)
    #inst = inst.set_index('endDate')

## Income statement variables to extract ##

# Total Revenue#
total_revenue = inst['totalRevenue']
avg_total_revenue = stat.mean(total_revenue)

# Operating Income
operating_income = inst['operatingIncome']
avg_operating_income = stat.mean(operating_income)

# Total Operating Expenses
total_operating_expenses = inst['totalOperatingExpenses']
avg_total_operating_expenses = stat.mean(total_operating_expenses)

# EBIT
ebit = (avg_total_revenue-avg_total_operating_expenses)

# Interest Expense
interest_expense = inst['interestExpense']
avg_interest_expense = stat.mean(interest_expense)


## Cash Flow variables to extract
fcf = format((cash['totalCashFromOperatingActivities'][0]) - abs(cash['capitalExpenditures'][0]), ',d')

## Parameters ##
opm = (avg_operating_income) / (avg_total_revenue)
roce = (ebit) / ((avg_total_assets) - (avg_total_current_liabilities))
leverage = (avg_total_liabilities) / (avg_total_assets)
interest_cover = (avg_operating_income) / (avg_interest_expense)
interest_cover = abs(interest_cover)

print("leverage: " + str(round(leverage,2)))
print("roce: " + str(round(roce,2)))
print("opm: " + str(round(opm,2)))
print("interest cover: " + str(round(interest_cover, 2)))
print("last year's fcf: " + str(fcf))
#print(cash.columns.values)
#print(cash['totalCashFromOperatingActivities'])

## Save to file ##
    #print("Hello!")
        #if leverage < 1.00 and roce >= 0.2 and opm >= 0.2:
            #print("Sibna xa haga bello!")
            #outfile = open("DAX_results.txt", "a")
            #outfile.write(stock)
            #outfile.write("\n")
            #outfile.close()
        #else:
            #print("M'haw xej xbin!")
    #except AttributeError:
            #continue
