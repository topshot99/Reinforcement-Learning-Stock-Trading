import yfinance as yf
import os
import pandas as pd
#
# # Define a list of Nifty 50 stock symbols
# nifty50_symbols = ["ADANIENT.NS","ADANIPORTS.NS","APOLLOHOSP.NS","ASIANPAINT.NS","AXISBANK.NS","BAJAJ-AUTO.NS","BAJAJFINSV.NS","BPCL.NS","BHARTIARTL.NS","BRITANNIA.NS","CIPLA.NS","COALINDIA.NS","DIVISLAB.NS","DRREDDY.NS","EICHERMOT.NS","GRASIM.NS","HCLTECH.NS","HDFCBANK.NS","HDFCLIFE.NS","HEROMOTOCO.NS","HINDALCO.NS","HINDUNILVR.NS","HDFC.NS","ITC.NS","ICICIBANK.NS","INDUSINDBK.NS","INFY.NS","JSWSTEEL.NS","KOTAKBANK.NS","LT.NS","M&M.NS","MARUTI.NS","NESTLEIND.NS","NTPC.NS","ONGC.NS","POWERGRID.NS","RELIANCE.NS","SBILIFE.NS","SBIN.NS","SUNPHARMA.NS","TCS.NS","TATACONSUM.NS","TATAMOTORS.NS","TATASTEEL.NS","TATASTEEL.NS","TECHM.NS","TITAN.NS","ULTRACEMCO.NS","UPL.NS","WIPRO.NS"]
#
# # Define the start and end dates for the data
# start_date = "2018-01-01"
# end_date = "2023-9-14"
#
# # Loop through the Nifty 50 stock symbols and download their data
# for symbol in nifty50_symbols:
#     data = yf.download(symbol, start=start_date, end=end_date)
#     data.to_csv(os.path.join("data", symbol+".csv"))

# Test data download
start_date_test = "2022-09-14"
end_date_test = "2023-09-14"
nifty50_symbols_test = ["INDIGO"]
for symbol in nifty50_symbols_test:
    data = yf.download(symbol + ".NS", start=start_date_test, end=end_date_test)
    data.to_csv(os.path.join("test_data", symbol+".csv"))