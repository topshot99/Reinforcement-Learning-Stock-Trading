import yfinance as yf
import os

# Get the data for Hindustan Unilever from 2000 to 2015
data = yf.download("HINDUNILVR.NS", start="2000-01-01", end="2015-12-31")

# Select the desired columns
data = data[["Date", "Open", "High", "Low", "Close", "Volume"]]

# Save the data to a CSV file in the data folder

data.to_csv(os.path.join("data", "HINDUNILVR.csv"))