# inverter os valores e chaves de um dicionário

prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
}

prices_invertido = list(zip(prices.values(), prices.keys()))
for t in prices_invertido:
       print(t)
