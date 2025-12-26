def simple_moving_average_strategy(data, window=5):
    """
    Estrategia simple basada en media móvil.
    """

    close_prices = data["Close"]
    sma = close_prices.rolling(window=window).mean()

    # Extraemos valores escalares (números reales)
    last_close = close_prices.iloc[-1].item()
    last_sma = sma.iloc[-1].item()

    # Validamos datos suficientes
    if last_sma != last_sma:
        return "SIN DATOS SUFICIENTES"

    if last_close > last_sma:
        return "COMPRAR"
    else:
        return "NO COMPRAR"
