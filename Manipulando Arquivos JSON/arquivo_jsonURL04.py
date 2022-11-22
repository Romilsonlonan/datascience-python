import json
import os
from urllib.request import urlopen



response = urlopen("http://vimeo.com/api/v2/video/57733101.json").read().decode('utf8')
data = json.loads(response)[0]

arquivo_fonte = 'arquivos/dados.json'
arquivo_destino = 'arquivos/json_data.txt'

#print('Título: ', data['title'])
#print('URL: ', data['url'])
#print('Duração: ', data['duration'])
#print('Numeros que gostaram : ', data['stats_number_of_likes'])

