def calculate_metrics(results):
    trades= results['trades']
    equity_curve= results['equity_curve']
    initial_capital= results['initial_capital']
    final_capital= results['final_capital']

    # Retorno total
    total_return = (final_capital - initial_capital) / initial_capital * 100

    # Trades
    buy_trades = [t for t in trades if t[0] == 'BUY']
    sell_trades = [t for t in trades if t[0] == 'SELL']

    total_trades = min(len(buy_trades), len(sell_trades))

    wins = 0
    losses = 0

    for buy, sell in zip(buy_trades, sell_trades):
        if sell[1] > buy[1]:
            wins += 1
        else:
            losses += 1

    win_rate = (wins / total_trades * 100) if total_trades > 0 else 0

    # Drawdown (protegido)
    if not equity_curve:
        max_drawdown = 0
    else:
        peak = equity_curve[0] 
        max_drawdown = 0

    for value in equity_curve:
        if value > peak:
            peak = value
        drawdown = (peak - value) / peak * 100
        max_drawdown = max(max_drawdown, drawdown)

    return {
        'total_return_pct': total_return,
        'total_trades': total_trades,
        'wins': wins,
        'losses': losses,
        'win_rate_pct': win_rate,
        'max_drawdown_pct': max_drawdown
    }