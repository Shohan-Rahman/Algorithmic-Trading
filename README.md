Algorithmic Trading Adventure
Overview
Algorithmic Trading Adventure is a Python-based interactive project that simulates a simple moving-average crossover trading strategy.
It downloads real stock market data from Yahoo Finance, generates buy/sell signals using moving averages, executes simulated trades, and visualizes the performance using Matplotlib.
Features
* Automatically downloads stock data using Yahoo Finance (yfinance)

* Implements a Golden Cross / Death Cross strategy:

   * Golden Cross → Buy when the 50-day moving average crosses above the 200-day moving average

   * Death Cross → Sell when the 50-day moving average crosses below the 200-day moving average

      * Simulates trades with a customizable budget

      * Evaluates profit or loss based on trading activity

      * Visualizes closing prices, moving averages, and buy/sell signals using Matplotlib

      * User-friendly command-line interface
Requirements
Make sure you have Python 3.8 or later and install the following dependencies:
pip install yfinance pandas matplotlib








How to Run
         1. Save the file Algorithmic_Trading_Adventure.py in your working directory.

         2. Open a terminal or command prompt in that directory.
         3. Run the program with:

python Algorithmic_Trading_Adventure.py

         4. Follow the on-screen prompts:

            * Enter your name

            * Enter a stock symbol

            * Provide a start and end date (format: YYYY-MM-DD)

            * Input your budget

            * Choose between:

               * Option 1: Evaluate profit or loss

               * Option 2: Exit

________________


Example Session
What is your name: Alex
------Welcome Alex to Trading Adventure-------
Enter stock symbol: AAPL
Enter start date (YYYY-MM-DD): 2022-01-01
Enter end date (YYYY-MM-DD): 2023-01-01
What is your budget Alex: 10000
Which action you need?
1 : Evaluate profit or loss
2 : Exit
Enter option: 1
BUY 59 shares at $170.50
SELL 59 shares at $175.30 | Profit: $283.00
Initial Budget: 10000
Final Portfolio Value: 10283.0
Total Profit: $283.0


A Matplotlib window will also open showing:
                  * The stock’s closing price

                  * 50-day and 200-day moving averages

                  * Buy (green arrows) and Sell (red arrows) signals
Md. Shohanur Rahman Shohan
