from re import T


def fahrenheit(T):
    return((float(9)/5)*T + 32)


def celsius(T):
    return ((float(9)/5)*T + 32)


temperaturas = [0, 22.5, 40, 100]

map(fahrenheit, temperaturas)
list(map(fahrenheit, temperaturas))

print(list(map(fahrenheit, temperaturas)))