"""
O método Python replace é usado para substituir trechos de uma string por uma ou mais vezes. 
Também podemos utilizar o módulo re, no qual podemos aplicar expressões regulares para refinar 
ainda mais as condições de substituição. Portanto, a linguagem oferece diversos recursos para 
a manipulação de strings.
"""

import datetime

d1 = datetime.date(2022,11,28)
d2 = d1.replace(year=2021)

print('d1: ', d1)

print('d2: ', d2)

print (d1 - d2)