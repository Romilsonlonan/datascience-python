"""
Requests no Python serve para fazer uma requisição no Python como o próprio nome já
diz. É muito utilizada para fazer uma requisição na API que estiver utilizando, seja ela 
qual for.

O módulo Urllib é o módulo de manipulação de URL para python. É usado para buscar URLs 
(Uniform Resource Locators). Ele usa a função urlopen e é capaz de buscar URLs usando 
uma variedade de protocolos diferentes.
"""

import urllib.request

# Variável resposta armazena o objeto da conexão  à url passada como parâmentro 
resposta = urllib.request.urlopen('http://python.org')

print(resposta)

html = resposta.read()

print(html)