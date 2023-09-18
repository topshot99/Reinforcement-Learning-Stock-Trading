import pandas as pd
import numpy as np
import os
from stable_baselines3 import A2C

model = A2C.load("trading_agent")

# Initialize variables for tracking trading performance
initial_balance = 100000  # Starting balance 1L
balance = initial_balance
positions = [-1,0,1]
position = 0  # 0 for no position, 1 for long (buy), -1 for short (sell)
net_profit = 0


def trading_logic(day_data):
    observation = [
        row['open'],
        row['high'],  # Highest price of the day
        row['low'],  # Lowest price of the day
        row['close'],  # Closing price
        row['volume'],  # Trading volume
        position,
        position
    ]
    return model.predict(np.array(observation))


# Load historical data
data = pd.read_csv(os.path.join('./test_data', "INDIGO.csv"))
df = pd.DataFrame()
df["close"] = data["Close"].pct_change()
df["open"] = data["Open"] / data["Close"]
df["high"] = data["High"] / data["Close"]
df["low"] = data["Low"] / data["Close"]
df["volume"] = data["Volume"] / data["Volume"].rolling(3).max()
df["close_price"] = data["Close"]
df.dropna(inplace=True)

# Iterate over each day's data
for index, row in df.iterrows():
    position = positions[trading_logic(row)[0]]  # Determine trading action based on your strategy
    print("action: ", position)
    print("initial balance: ", balance)
    # Execute the trading action
    if position == 1:  # Buy
        balance -= row['close_price']  # Deduct the purchase cost
    elif position == -1:  # Sell
        balance += row['close_price']  # Add the selling price
    print("later balance: ", balance)

# Calculate the net profit margin
net_profit = (balance - initial_balance) / initial_balance * 100  # As a percentage

# Print the result
print(f"Net Profit Margin: {net_profit:.2f}%")
