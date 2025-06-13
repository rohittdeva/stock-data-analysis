# 📈 Stock Price Analysis and Forecasting of Top 3 Indian Stocks

This is an interactive web application built using **Streamlit** to analyze and forecast stock prices of **Reliance Industries**, **Tata Consultancy Services (TCS)**, and **HDFC Bank**. The application provides multiple types of analysis to help users make informed investment decisions.

---

## 🔍 Features

### 1. Descriptive Analysis
- Summary statistics: mean, median, standard deviation
- Visual trends of stock prices over time

### 2. Diagnostic Analysis
- Daily returns, volatility, and risk
- Histograms and KDE plots for return distribution

### 3. Prescriptive Analysis
- Buy/Sell signals using 40-day and 100-day moving average crossover strategy

### 4. Comparative Analysis
- Normalized visual comparison of all 3 stocks on one plot

---

## 📊 Tech Stack

- **Python**
- **Streamlit** for the web interface
- **yfinance** for stock data fetching
- **statsmodels** for ARIMA time series modeling
- **scikit-learn**, **matplotlib**, **seaborn**, **pandas**, **numpy**

---

## 🛠 How to Run

1. **Clone the repository**

\`\`\`bash
git clone https://github.com/rohittdeva/stock-data-analysis.git
cd stock-analysis-streamlit
\`\`\`

2. **Install the dependencies**

\`\`\`bash
pip install -r requirements.txt
\`\`\`

3. **Run the Streamlit app**

\`\`\`bash
streamlit run app.py
\`\`\`

---

## 📁 Project Structure

\`\`\`
├── app.py                  # Main Streamlit app
├── requirements.txt        # Python dependencies
├── README.md               # Project overview
├── Project Documentation.pdf  # Project report
\`\`\`

---

## 📚 References

- [Yahoo Finance API (yfinance)](https://pypi.org/project/yfinance/)
- [Streamlit Docs](https://docs.streamlit.io/)
- [ARIMA - Statsmodels](https://www.statsmodels.org/stable/index.html)
- [Scikit-learn](https://scikit-learn.org/)

---

## 🧑‍💻 Author

**Rohitt Kumar D**  
Postgraduate Student in Computer Science  
📫 rohittkumard@gmail.com  
[GitHub](https://github.com/rohittdeva) | [LinkedIn](https://linkedin.com/in/rohittkumard)

---

## 📌 License

This project is open-source and available under the MIT License.
