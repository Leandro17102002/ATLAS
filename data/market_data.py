import yfinance as yf
import pandas as pd

def get_historical_data(ticker, start_date, end_date):
    """
    Descarga datos historicos diarios de una accion
    """
    data = yf.download(ticker, start=start_date, end=end_date, interval='1d')
    # hig - low
    high_low = data['High'] - data['Low']

    #high - close anterior
    high_close = (data['High'] - data['Close'].shift()).abs()

    #low - close anterior
    low_close = (data['Low'] - data['Close'].shift()).abs()

    # True range (El mayor de los 3)
    true_range = pd.concat([high_low, high_close, low_close], axis=1).max(axis=1)

    data['ATR'] = true_range.rolling(14).mean()

    print(data[["Close", "ATR"]].tail())

    return data