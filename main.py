from data.market_data import get_historical_data
from strategy.simple_strategy import simple_moving_average_strategy

def main():
    print("Trading bot iniciado correctamente")
    
    symbol = "AAPL"
    start_date = "2023-01-01"
    end_date= "2023-03-01"

    data=get_historical_data(symbol, start_date, end_date)
    print("Datos historicos descargados:")
    print(data.head()) # Muestra las primeras filas

if __name__== "__main__":
    main()  # Ejecuta esto solo si este archivo es el principal