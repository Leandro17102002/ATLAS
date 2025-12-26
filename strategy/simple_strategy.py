def simple_moving_average_strategy(data, window=5):
    """
    Estrategia simple basada en media movil
    """

    data['SMA'] = data['Close'].rolling(window=window).mean()
    last_close=data['Close'].iloc[-1]
    last_sma=data['SMA'].iloc[-1]

    if last_close > last_sma:
        return 'COMPRAR'
    else:
        return 'NO COMPRAR'