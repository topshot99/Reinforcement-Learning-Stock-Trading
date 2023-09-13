import yfinance as yf
import os

# Get the data for Hindustan Unilever from 2000 to 2015
data = yf.download("HINDUNILVR.NS", start="2016-01-01", end="2018-12-31")

# Save the data to a CSV file in the data folder

data.to_csv(os.path.join("test_data", "HINDUNILVR.csv"))