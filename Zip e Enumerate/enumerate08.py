seasons = ['Spring', 'Summer', 'Fall', 'Winter']

# retorna um objeto iterável, aplicar para list
print (enumerate(seasons, start=1))
# <enumerate object at 0x7f0bc054c5c0>

print (list(enumerate(seasons, start=2)))