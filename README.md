# 📊 NextEra Energy (NEE) Stock Analysis  
### **AI Infrastructure Surge • Long-Term Wealth Creation • Renewable Energy Cycles**  
**Dataset:** Kaggle  
**Period:** 1973–2026  

---

## 📁 Project Overview

This project analyzes the long-term stock performance of **NextEra Energy (NEE)** using historical data obtained from Kaggle. The study focuses on three major objectives:

1. **AI Infrastructure Surge Impact (2024–2025)**  
   Identify whether the global rise in AI data centers increased NEE's stock volatility.

2. **Long-Term Wealth Creation Potential**  
   Measure price compounding using CAGR and portfolio simulation.

3. **Renewable Energy Cycles Behavior**  
   Analyze how NEE performs across economic cycles, interest-rate periods, and renewable policy shifts.

The analysis uses time-series methods, rolling volatility, yearly returns, and growth modeling.

---

## 🧰 Technologies Used

- Python  
- Pandas  
- NumPy  
- Matplotlib 

---

## 📂 Dataset Description

- **Source:** Kaggle  
- **Company:** NextEra Energy (NEE)  
- **Data Type:** Daily stock prices  
- **Columns Used:** Date, Open, High, Low, Close, Volume  
- **Time Period:** 1973–2026  

This dataset provides enough historical depth to perform long-term volatility and return studies.


## ⚙️ Analysis Workflow

### **1. Data Preparation**
- Date column converted to `datetime`  
- Sorted chronologically  
- Date set as index  
- Computed daily returns using `pct_change()`  
- Cleaned NaN values  

---

### **2. AI Infrastructure Surge — Volatility Analysis**

We analyzed **90-day annualized rolling volatility** to study the effect of AI-driven energy demand around 2024–2025.

#### 📌 Volatility Comparison Table

| Period | Avg Rolling Volatility (90-Day) |
|--------|---------------------------------|
| **Before 2024** | 0.1971 |
| **After 2024** | 0.2767 |

This represents a **~40% increase** in average volatility.

#### 🔍 Insight
- The volatility graph shows a **clear spike after 2024**.
- This indicates a **structural break in stock volatility**, likely linked to the explosive increase in AI data center power requirements.
- The market priced higher uncertainty into energy-related stocks.

---

### **3. Long-Term Wealth Creation Analysis**

A simulated portfolio of **₹10,000 / $10,000** was analyzed using year-end closing prices.

#### 📌 CAGR Result
**CAGR = 7.79%**

#### 📈 Insight
- The investment grows steadily over decades.
- After 2000, growth accelerates sharply.
- The portfolio crosses **₹600,000+** around 2021.
- Confirms NEE as a strong long-term compounder.

---

### **4. Renewable Energy Cycles — Annual Return Analysis**

We calculated annual returns using `.resample("Y")` to observe cycle-based behavior.

#### 📊 Key Observations
- Several years show very strong positive returns (+40% to +70%).  
- Downturns occur during:
  - Economic recessions  
  - High interest-rate periods  
  - Policy uncertainty  
- NEE consistently **recovers strongly** after declines.

#### 🔍 Insight
NEE’s performance is cyclical but **structurally positive**, matching long-term renewable energy trends.

---

## 🧩 Final Insights Summary

### ✔ **AI Surge Impact**
Volatility sharply increased post-2024, confirming the market's reaction to AI-related energy demand.

### ✔ **Long-Term Wealth Creation**
NEE shows strong compounding with ~7.8% CAGR, making it a robust long-term investment.

### ✔ **Renewable Energy Cycles Behavior**
Returns fluctuate due to macroeconomic factors but maintain long-term upward tendency.

---

## 🏁 Conclusion

NextEra Energy demonstrates:

- **Higher volatility during technological disruptions** (AI infrastructure boom)  
- **Strong and stable long-term wealth creation**  
- **Resilience across renewable energy and interest-rate cycles**  

This project demonstrates your ability to perform time-series financial analysis, identify structural market changes, and extract actionable insights from data.

---

## 📜 Project Deliverables

- Python Analysis Script  
- PDF Report   
- README.md (this file)

---

## 🚀 Future Enhancements

- Price forecasting using ARIMA or Prophet  
- Structural break detection using CUSUM / BOCPD  
- Comparison with other renewable energy companies  
- News sentiment analysis for event impact  

---

