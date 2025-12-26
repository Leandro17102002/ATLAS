import yfinance as yf
import pandas as pd

def get_historical_data(symbol, start_date, end_date):
    """
    Descarga datos historicos diarios de una accion
    """
    data=yf.download(
        symbol,
        start=start_date,
        end=end_date,
        interval='1d'
    )
    return data