def run_backtest(data, window=5, initial_capital=10000):
    '''
    Backtesting simpole de estrategia SMA.
    '''

    capital = initial_capital
    position = 0  # cantidad de acciones

    close_prices = data['Close']
    sma = close_prices.rolling(window=window).mean()

    trades = []
    equity_curve = []

    for i in range (window, len(data)):
        price = close_prices.iloc[i].item()
        current_sma = sma.iloc[i].item()

        # Si no hay SMA valida, seguimos
        if current_sma != current_sma:
            continue

        # Condicion de compra
        if position == 0 and price > current_sma:
            position = capital/price
            capital = 0
            trades.append(('BUY', price))

        # condicion de venta
        elif position > 0 and price < current_sma:
            capital = position * price
            position = 0
            trades.append(('SELL', price))

    # Si queda posision abierta, la cerramos al final
    if position > 0:
        final_price= close_prices.iloc[-1].item()
        capital = position * close_prices.iloc[-1].item()
        trades.append(('SELL', final_price))
    
    return {
        'final_capital': capital,
        'trades': trades,
        'equity_curve': equity_curve,
        'initial_capital': initial_capital
    }