from data.market_data import get_historical_data
from backtest.simple_backstest import run_backtest
from metrics.performance import calculate_metrics

def main():
    print("Trading bot iniciado correctamente \n")
    
    symbol = "AAPL"
    start_date = "2022-01-01"
    end_date= "2023-12-31"

    data=get_historical_data(symbol, start_date, end_date)
    
    results = run_backtest(data)
    metrics = calculate_metrics(results)

    initial_capital = results['initial_capital']
    final_capital = results['final_capital']

    print(f"💰 Capital inicial: ${initial_capital:,.2f}") 
    print(f"💰 Capital final:   ${final_capital:,.2f}\n")

    print("📊 MÉTRICAS DEL BACKTEST\n")

    print(f"Retorno total: {metrics.get('total_return_pct', 0):.2f}%")
    print(f"Total trades: {metrics.get('total_trades', 0)}")
    print(f"Ganadoras: {metrics.get('wins', 0)}")
    print(f"Perdedoras: {metrics.get('losses', 0)}")
    print(f"Win rate: {metrics.get('win_rate_pct', 0):.2f}%")
    print(f"Máx. drawdown: {metrics.get('max_drawdown_pct', 0):.2f}%")




if __name__== "__main__":
    main()  # Ejecuta esto solo si este archivo es el principal