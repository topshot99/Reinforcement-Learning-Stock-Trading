import gymnasium as gym
import json
import datetime as dt
from stable_baselines3.common.env_util import make_vec_env

from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3 import PPO
from stable_baselines3.ppo import MlpPolicy

from env.StockTradingEnv import StockTradingEnv

import pandas as pd

df = pd.read_csv('./data/HINDUNILVR.csv')
df = df.sort_values('Date')

# Define your render_mode, e.g., 'human' or 'rgb_array'
render_mode = 'human'
# The algorithms require a vectorized environment to run
env = DummyVecEnv([lambda: StockTradingEnv(df)])

model = PPO(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=20000)
print("training completed")
obs = env.reset()
for i in range(2000):
    print("starting step: ", i)
    action, _states = model.predict(obs)
    obs, rewards, done, info = env.step(action)
    env.render(mode=render_mode)
