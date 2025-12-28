def run_backtest(data, window=20, initial_capital=10000):
    cash = initial_capital
    risk_per_trade = 0.01
    position = 0
    stop_loss = None

    close_prices = data['Close']
    sma = close_prices.rolling(window=window).mean()

    trades = []
    equity_curve = []

    for i in range(window, len(data)):
        price = close_prices.iloc[i].item()
        current_sma = sma.iloc[i].item()

        if current_sma != current_sma:
            continue

        # STOP LOSS
        if position > 0 and price <= stop_loss:
            cash += position * price
            position = 0
            stop_loss = None
            trades.append(('STOP_LOSS', price))

        # COMPRA
        elif position == 0 and price > current_sma:
            atr = data['ATR'].iloc[i].item()

            risk_amount = cash * risk_per_trade
            risk_per_share = 2 * atr

            position_size = risk_amount / risk_per_share
            cost = position_size * price

            if cost <= cash:
                position = position_size
                cash -= cost
                stop_loss = price - (2 * atr)
                trades.append(('BUY', price))

        # VENTA NORMAL
        elif position > 0 and price < current_sma:
            cash += position * price
            position = 0
            stop_loss = None
            trades.append(('SELL', price))

        equity_curve.append(cash + position * price)

    if position > 0:
        cash += position * close_prices.iloc[-1].item()
        trades.append(('SELL', close_prices.iloc[-1].item()))
        equity_curve.append(cash)

    return {
        'final_capital': cash,
        'trades': trades,
        'equity_curve': equity_curve,
        'initial_capital': initial_capital
    }
