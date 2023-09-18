import gymnasium as gym
import pandas as pd
import gym_trading_env
import os
from stable_baselines3 import A2C

def preprocess(df, inplace=True):
    new_columns = {"Date":"date","Open":"open","High":"high","Low":"low","Close":"close","Adj Close":"adj_close","Volume":"volume"}
    # df is a DataFrame with columns : "open", "high", "low", "close", "volume"
    df.rename(columns=new_columns,inplace=True)
    # Create the feature : ( close[t] - close[t-1] )/ close[t-1]
    df["feature_close"] = df["close"].pct_change()
    # Create the feature : open[t] / close[t]
    df["feature_open"] = df["open"]/df["close"]
    # Create the feature : high[t] / close[t]
    df["feature_high"] = df["high"]/df["close"]
    # Create the feature : low[t] / close[t]
    df["feature_low"] = df["low"]/df["close"]
    # Create the feature : volume[t] / max(*volume[t-7*24:t+1])
    df["feature_volume"] = df["volume"] / df["volume"].rolling(7*24).max()

    df.dropna(inplace= True) # Clean again !
    return df.copy()
#df = pd.read_csv('./data/HINDUNILVR.csv')
#df=preprocess(df)
#df.to_pickle('your_data.pkl')
# Eatch step, the environment will return 5 inputs  : "feature_close", "feature_open", "feature_high", "feature_low", "feature_volume"
data_dir = 'data'

# Loop through all the CSV files in the directory
for filename in os.listdir(data_dir):
    if filename.endswith('.csv'):
        # Load the CSV file into a pandas DataFrame
        df = pd.read_csv(os.path.join(data_dir, filename))
        df=preprocess(df)
        # Preprocess the data as needed
        # ...
        
        # Save the preprocessed data as a pickle file
        df.to_pickle(os.path.join(data_dir, filename[:-4] + '.pkl'))


env = gym.make(
    "MultiDatasetTradingEnv",
    preprocess=preprocess,
    dataset_dir= 'data/*.pkl',
    name= "BTCUSD",
    positions = [ -1, 0, 1], # -1 (=SHORT), 0(=OUT), +1 (=LONG)
    trading_fees = 0.01/100, # 0.01% per stock buy / sell (Binance fees)
    borrow_interest_rate= 0.0003/100, # 0.0003% per timestep (one timestep = 1h here)
    )

# Create an RL agent with A2C algorithm and MlpPolicy
model = A2C("MlpPolicy", env, verbose=1)  # You can adjust hyperparameters here
# Train the agent (adjust the number of training steps)
model.learn(total_timesteps=int(1e4))

# Run an episode until it ends :
done, truncated = False, False
observation, info = env.reset()

print("Observation: ")
print(observation)
while not done and not truncated:
    # Use the trained agent to select an action (buy, sell, hold)
    # Pick a position by its index in your position list (=[-1, 0, 1])....usually something like : position_index = your_policy(observation)
    action, _ = model.predict(observation)
    # Execute the chosen action in the live environment
    observation, reward, done, truncated, info = env.step(action)
    # position_index = env.action_space.sample() # At every timestep, pick a random position index from your position list (=[-1, 0, 1])
    # observation, reward, done, truncated, info = env.step(position_index)

# # Optionally, save the trained model for later use
# # can be loaded using model = A2C.load("trained_trading_agent")
model.save("trading_agent")