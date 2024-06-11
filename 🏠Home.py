import streamlit as st
import yfinance as yf
import datetime

st.header("My Finance App")

symbol = st.sidebar.text_input("Enter a stock symbol", value="AAPL")

mid_value = st.sidebar.slider('Slide me', min_value=0, max_value=100)


st.title(f"Stock price of {symbol}")

start_date = st.sidebar.date_input("Start date", value=datetime.date(2023, 1, 1))
end_date = st.sidebar.date_input("Start date", value=datetime.date(2024, 1, 1))

df = yf.download(symbol, start=start_date, end=end_date)

st.line_chart(df["Close"])

st.subheader("Volume")

st.write(df)