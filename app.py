import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load Data
data = pd.read_csv('close_prices.csv', parse_dates=['Date'])
data.set_index('Date', inplace=True)
data = data.ffill()

st.title("Stock Data Analysis Tool")
st.write("An interactive tool for analyzing and forecasting stock price data.")

# Select stock(s)
stock_options = st.multiselect("Select stock(s) to analyze", options=data.columns)

# 1. Descriptive Analysis
st.header("1. Descriptive Analysis")
st.write("The Descriptive Analysis section provides summary statistics and visualizes stock price trends over time, "
         "helping you understand the general performance and volatility of each selected stock.")

if stock_options:
    for stock in stock_options:
        st.subheader(f"Descriptive Statistics for {stock}")
        
        # Calculate summary statistics
        stats = data[stock].describe()
        st.write(stats)  # Display summary statistics
        
        # Plot price trend
        st.subheader("Price Trend")
        plt.figure(figsize=(10, 5))
        plt.plot(data[stock], label=f"{stock} Price")
        plt.title(f"{stock} Price Trend")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        st.pyplot(plt)  # Display price trend plot

# 2. Diagnostic Analysis
st.header("2. Diagnostic Analysis")
st.write("The Diagnostic Analysis section identifies patterns in the stock’s returns. It provides a distribution of daily "
         "returns and highlights the most volatile days, offering insights into the risk profile of the stock.")

if stock_options:
    for stock in stock_options:
        st.subheader(f"Diagnostic Analysis for {stock}")
        
        # Calculate daily returns
        data[f'{stock}_Returns'] = data[stock].pct_change() * 100
        
        # Plot returns distribution
        st.subheader("Daily Returns Distribution")
        plt.figure(figsize=(10, 5))
        plt.hist(data[f'{stock}_Returns'].dropna(), bins=50, alpha=0.5, color='blue', density=True)
        data[f'{stock}_Returns'].plot(kind='kde', color='red')  # KDE plot
        plt.title(f"{stock} Returns Distribution")
        plt.xlabel("Daily Returns (%)")
        plt.ylabel("Frequency")
        st.pyplot(plt)
        
        # Display top 5 most volatile days
        top_volatile_days = data[f'{stock}_Returns'].abs().nlargest(5)
        st.write("Top 5 Most Volatile Days:")
        st.write(top_volatile_days)

# 3. Prescriptive Analysis
st.header("3. Prescriptive Analysis (Moving Average Crossover Strategy)")
st.write("The Prescriptive Analysis section provides actionable investment strategies based on the moving average crossover. "
         "It indicates buy and sell signals, helping to guide potential investment decisions.")

if stock_options:
    for stock in stock_options:
        st.subheader(f"Prescriptive Analysis for {stock}")
        
        # Calculate moving averages
        data[f'{stock}_Short_MA'] = data[stock].rolling(window=40).mean()
        data[f'{stock}_Long_MA'] = data[stock].rolling(window=100).mean()
        
        # Generate buy/sell signals
        data['Signal'] = 0
        data['Signal'] = np.where(data[f'{stock}_Short_MA'] > data[f'{stock}_Long_MA'], 1, 0)
        data['Signal'] = data['Signal'].diff()  # 1 for buy, -1 for sell when crossing occurs

        # Plot moving averages with buy/sell signals
        st.subheader("Moving Average Crossover Plot")
        plt.figure(figsize=(10, 5))
        plt.plot(data[stock], label="Price", color="blue")
        plt.plot(data[f'{stock}_Short_MA'], label="40-Day MA", color="orange")
        plt.plot(data[f'{stock}_Long_MA'], label="100-Day MA", color="green")
        
        # Plot buy signals
        plt.plot(data[data['Signal'] == 1].index, 
                 data[f'{stock}_Short_MA'][data['Signal'] == 1], 
                 '^', markersize=10, color='green', label='Buy Signal')

        # Plot sell signals
        plt.plot(data[data['Signal'] == -1].index, 
                 data[f'{stock}_Short_MA'][data['Signal'] == -1], 
                 'v', markersize=10, color='red', label='Sell Signal')
        
        plt.title(f"{stock} Moving Average Crossover Strategy")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        st.pyplot(plt)

# 4. Comparative Analysis
st.header("4. Comparative Analysis")
st.write("The Comparative Analysis section allows for a side-by-side comparison of multiple stocks' price trends, "
         "helping users quickly assess which stocks have performed better over the same period.")

if stock_options and len(stock_options) > 1:
    st.subheader("Comparative Price Trend Analysis")
    
    # Plot selected stocks in a single plot
    plt.figure(figsize=(10, 5))
    for stock in stock_options:
        plt.plot(data[stock], label=stock)
    plt.title("Comparative Analysis of Selected Stocks")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    st.pyplot(plt)
