# fython
A Python script to screen high-quality companies

This is a simple script I wrote to help me screen good quality stocks quickly.
The script is able to fetch stock data from Yahoo Finance. This was made possible
through the use of Yahoo Query, a Python wrapper for an unofficial Yahoo Finance API.

https://github.com/dpguthrie/yahooquery

https://yahooquery-streamlit.herokuapp.com/

The singlestockquery script works simply by inputting the Yahoo ticker symbol into the Ticker().

This ticker will vary across different exchange a stock is listed on.

At present, the script output includes:
dividend
yield
ex-dividend date
payout ratio
forward p/e
leverage (debt:asset ratio)
roce
opm (operating profit margin)
interest cover
last year's fcf

The script can be tweaked according to your liking to include more financial variables.
