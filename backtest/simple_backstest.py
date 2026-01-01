def run_backtest(data, window=20, initial_capital=10000):
    cash = initial_capital
    risk_per_trade = 0.01
    position = 0
    stop_loss = None
    take_profit = None

    close_prices = data['Close']
    sma = close_prices.rolling(window=window).mean()

    trades = []
    equity_curve = []
    
    completed_trades=[]
    entry_price = None
    entry_position = None


    for i in range(window, len(data)):
        price = close_prices.iloc[i].item()
        current_sma = sma.iloc[i].item()

        if current_sma != current_sma:
            continue

        # STOP LOSS
        if position > 0 and stop_loss is not None and price <= stop_loss:
            cash += position * price
            
            pnl = (price - entry_price) * entry_position
            completed_trades.append(pnl)
            
            position = 0
            stop_loss = None
            take_profit = None
            entry_price = None
            entry_position = None

            trades.append(('STOP_LOSS', price))

        # TAKE PROFIT
        elif position > 0 and take_profit is not None and price >= take_profit:
            cash += position * price

            pnl = (price - entry_price) * entry_position
            completed_trades.append(pnl)

            position = 0
            stop_loss = None
            take_profit = None
            entry_price = None
            entry_position = None

            trades.append(('TAKE_PROFIT', price))
            continue


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
                entry_price = price
                entry_position = position
                stop_loss = price - (2 * atr)
                risk_per_share = price - stop_loss
                take_profit = price + (2 * risk_per_share)
                trades.append(('BUY', price))

        # VENTA POR SMA
        elif position > 0 and price < current_sma:
            cash += position * price

            pnl = (price - entry_price) * entry_position
            completed_trades.append(pnl)

            position = 0
            stop_loss = None
            take_profit = None
            entry_price = None
            entry_position = None

            trades.append(('SELL', price))

        equity_curve.append(cash + position * price)

    if position > 0:
        final_price = close_prices.iloc[-1].item()
        cash += position * final_price

        pnl = (final_price - entry_price) * entry_position
        completed_trades.append(pnl)

        trades.append(('SELL', close_prices.iloc[-1].item()))
        equity_curve.append(cash)

    return {
        'final_capital': cash,
        'trades': trades,
        'completed_trades': completed_trades,
        'equity_curve': equity_curve,
        'initial_capital': initial_capital
    }
