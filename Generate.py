import pandas as pd
import yfinance as yf

# List of companies and their tickers
companies = {
    'ASIANPAINT': 'ASIANPAINT.BO',
    'AXISBANK': 'AXISBANK.BO',
    'BAJAJFINSV': 'BAJAJFINSV.BO',
    'BAJFINANCE': 'BAJFINANCE.BO',
    'BHARTIARTL': 'BHARTIARTL.BO',
    'HCLTECH': 'HCLTECH.BO',
    'HDFCBANK': 'HDFCBANK.BO',
    'HINDUNILVR': 'HINDUNILVR.BO',
    'ICICIBANK': 'ICICIBANK.BO',
    'INDUSINDBK': 'INDUSINDBK.BO',
    'INFY': 'INFY.BO',
    'ITC': 'ITC.BO',
    'JSWSTEEL': 'JSWSTEEL.BO',
    'KOTAKBANK': 'KOTAKBANK.BO',
    'LT': 'LT.BO',
    'M&M': 'MM.BO',
    'MARUTI': 'MARUTI.BO',
    'NESTLEIND': 'NESTLEIND.BO',
    'NTPC': 'NTPC.BO',
    'POWERGRID': 'POWERGRID.BO',
    'RELIANCE': 'RELIANCE.BO',
    'SBIN': 'SBIN.BO',
    'SUNPHARMA': 'SUNPHARMA.BO',
    'TATAMOTORS': 'TATAMOTORS.BO',
    'TATASTEEL': 'TATASTEEL.BO',
    'TCS': 'TCS.BO',
    'TECHM': 'TECHM.BO',
    'TITAN': 'TITAN.BO',
    'ULTRACEMCO': 'ULTRACEMCO.BO',
    'WIPRO': 'WIPRO.BO',
}

# Define date range
start_date = '2023-04-01'
end_date = '2024-03-14'

# Create an empty DataFrame to store stock data
df = pd.DataFrame()

# Fetch historical stock data for each company and append to DataFrame
for company, ticker in companies.items():
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data['Company'] = company  # Add company name as a column
    df = pd.concat([df, stock_data])  # Concatenate the DataFrame with stock_data

# Save DataFrame to a CSV file
df.to_csv('bse_sensex_companies_stocks_fy22_fy23.csv')

print("CSV file created successfully.")
