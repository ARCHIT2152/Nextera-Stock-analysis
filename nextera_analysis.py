import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("NEXTera_stocks_data_1973_2026.csv")
df["Date"] = pd.to_datetime(df["Date"], dayfirst=True)
df = df.sort_values("Date")
df.set_index("Date", inplace=True)
df["Daily_Return"] = df["Close"].pct_change()
df.dropna(inplace=True)

df["Vol_30"] = df["Daily_Return"].rolling(30).std() * np.sqrt(252)
df["Vol_90"] = df["Daily_Return"].rolling(90).std() * np.sqrt(252)

pre_2024 = df[df.index < "2024-01-01"]
post_2024 = df[df.index >= "2024-01-01"]

print("AI INFRASTRUCTURE SURGE ANALYSIS")
print("Avg Volatility before 2024:", pre_2024["Vol_90"].mean())
print("Avg Volatility after 2024:", post_2024["Vol_90"].mean())

plt.figure(figsize=(12, 5))
plt.plot(df.index, df["Vol_90"], label="90-Day Volatility")
plt.axvline(pd.to_datetime("2024-01-01"), color="red", linestyle="--", label="Start of 2024")
plt.title("Rolling Volatility - AI Surge Effect")
plt.xlabel("Year")
plt.ylabel("Volatility")
plt.legend()
plt.show()

df["Year"] = df.index.year
yearly_close = df.groupby("Year")["Close"].last()

total_years = yearly_close.index[-1] - yearly_close.index[0]
cagr = (yearly_close.iloc[-1] / yearly_close.iloc[0]) ** (1 / total_years) - 1
print("\nWEALTH CREATION ANALYSIS")
print("Price CAGR:", round(cagr * 100, 2), "%")

initial_money = 10000
wealth = initial_money * (yearly_close / yearly_close.iloc[0])

plt.figure(figsize=(12, 5))
plt.plot(wealth.index, wealth.values)
plt.title("Long-Term Wealth Creation")
plt.xlabel("Year")
plt.ylabel("Portfolio Value")
plt.grid(True)
plt.show()

annual_returns = df["Close"].resample("Y").last().pct_change() * 100

plt.figure(figsize=(12, 5))
plt.bar(annual_returns.index.year, annual_returns.values)
plt.title("Annual Returns - Renewable Energy Cycles")
plt.xlabel("Year")
plt.ylabel("Annual Return (%)")
plt.show()

print("\nFINAL INSIGHTS")
print("- Volatility increased after 2024.")
print("- The stock shows strong long-term growth.")
print("- Renewable energy cycles create ups and downs but overall growth remains strong.")
