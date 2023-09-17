# Reinforcement Learning Stock Trading

This repository contains a reinforcement learning-based agent designed to navigate the stock market effectively.
The agent learns to make trading decisions by training on historical stock price data.

## Getting Started

Follow these steps to set up and use the RL stock trading agent:

1. **Fetch Historical Data**
   - Execute `python data-fetch.py` to fetch historical data for your desired stock. Replace the stock symbol and date range with your preferences in the script.

   ```bash
   python data-fetch.py 
   ```
   This script retrieves historical stock price data, which will be used for training and testing the model.
   - Next, run TradingEnv.py to train the reinforcement learning model using the fetched data. Ensure that you have all the required dependencies installed (see requirements.txt).
    ```bash
   python TradingEnv.py

   ``` 
   
2. **Using a Pretrained Model**
Alternatively, this repository provides a custom trained model (trading_agent.zip) that you can load and use directly if you prefer not to train your own model.

3. **Testing the Model with Live Data**
Run TestTradingEnv.py to evaluate the accuracy of the trained model when making trading decisions on live data.
```bash
python TestTradingEnv.py
```

## Additional Resources

- Open AI gym reference docs: https://gymnasium.farama.org/
- Feel free to explore and adapt the code to your specific needs in stock trading and reinforcement learning.

