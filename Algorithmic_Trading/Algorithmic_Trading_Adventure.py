import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

class Trade:
    def __init__(self, symbol, start_date, end_date):
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date
        self.data = None
        self.cash = 0
        self.shares = 0
        self.buy_price = 0

    # Set budget
    def set_budget(self, budget):
        self.cash = budget

    # Download and clean data
    def get_data(self):
        self.data = yf.download(self.symbol, start=self.start_date, end=self.end_date, auto_adjust=False)
        self.data.drop_duplicates(inplace=True)
        self.data.ffill(inplace=True)

    # Calculate moving averages
    def calculate_moving_averages(self):
        self.data["MA50"] = self.data["Close"].rolling(50).mean()
        self.data["MA200"] = self.data["Close"].rolling(200).mean()

    # Generate Buy or Sell Signals
    def generate_signals(self):
        self.data["Signal"] = 0
        self.data.loc[self.data["MA50"] > self.data["MA200"], "Signal"] = 1
        self.data["Change"] = self.data["Signal"].diff()

    # Golden/death cross.
    def trade(self):
        for i in range(len(self.data)):
            # Golden Cross → Buy
            if self.data["Change"].iloc[i] == 1 and self.shares == 0:
                self.buy_price = float(self.data.iloc[i]["Close"])
                self.shares = int(self.cash // self.buy_price)
                self.cash -= self.shares * self.buy_price
                print(f"BUY {self.shares} shares at ${self.buy_price:.2f}")

            # Death Cross → Sell
            elif self.data["Change"].iloc[i] == -1 and self.shares > 0:
                sell_price = float(self.data.iloc[i]["Close"])
                self.cash += self.shares * sell_price
                profit = (sell_price - self.buy_price) * self.shares
                print(f"SELL {self.shares} shares at ${sell_price:.2f} | Profit: ${profit:.2f}")
                self.shares = 0

        # Force close
        if self.shares > 0:
            final_price = float(self.data["Close"].iloc[-1])
            self.cash += self.shares * final_price
            profit = (final_price - self.buy_price) * self.shares
            print(f"FORCE SELL {self.shares} shares at ${final_price:.2f} | Profit: ${profit:.2f}")
            self.shares = 0

    # Evaluate profit or loss
    def evaluate(self, initial_budget):
        total_profit = self.cash - initial_budget
        print("\nInitial Budget:", initial_budget)
        print("Final Portfolio Value:", round(self.cash, 2))
        
        if total_profit > 0:
            print("Total Profit: $", round(total_profit, 2))
        elif total_profit < 0:
            print("Total Loss: $", abs(round(total_profit, 2)))
        else:
            print("No Profit, No Loss")

    # Matplot
    def plot_trades(self):
            plt.figure(figsize=(12,6))
            plt.plot(self.data['Close'], label='Close Price', color='blue')
            plt.plot(self.data['MA50'], label='MA50', color='orange')
            plt.plot(self.data['MA200'], label='MA200', color='green')

            # Plot buy/sell signals
            buy_signals = self.data[self.data['Change'] == 1]
            sell_signals = self.data[self.data['Change'] == -1]
            plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='green', label='Buy', s=100)
            plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='red', label='Sell', s=100)

            plt.title(f'{self.symbol} Trading Strategy')
            plt.xlabel('Date')
            plt.ylabel('Price')
            plt.legend()
            plt.show()


# --- User Interface ---

while True:
    name = input("What is your name: ")

    print(f"------Welcome {name} to Trading Adventure-------")

    print("Before start we need your Stock symble in which you trading and start to end date also.")
    symbol = input("Enter stock symbol: ")
    start = input("Enter start date (YYYY-MM-DD): ")
    end = input("Enter end date (YYYY-MM-DD): ")
    trader = Trade(symbol,start,end)

    budget = int(input(f"What is your budget {name}: "))
    trader.set_budget(budget)
    trader.get_data()
    trader.calculate_moving_averages()
    trader.generate_signals()

    print("Which action you need?")

    print("1 : Evaluate profit or loss")
    print("2 : Exit")

    ch = int(input("Enter option: "))

    if ch == 1:
        trader.trade()
        trader.evaluate(budget)
        trader.plot_trades()
        print("Thanks")
        break
    elif ch == 2:
        print("Thank you for visiting! Goodbye!")
        break
    else:
        print("Invalid option.")