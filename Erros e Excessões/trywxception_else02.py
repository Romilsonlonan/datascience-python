# Utilizando try, exceptions e else com arquivo sem extensão txt
try:
    f = open('arquivos/testendoerros','r')
except IOError:
    print("Erro: Arquivo não encontrado ou não pode ser lido.")
else:
    print("Conteúdo gravado com sucesso!")
    f.close()    