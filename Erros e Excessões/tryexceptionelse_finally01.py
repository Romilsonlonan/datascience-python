# Utilizando try, exceptions, else e finally 

try:
    f = open('arquivos/testendoerros.txt','w')
    f.write('Gravando no arquivo')
except IOError:
    print("Erro: Arquivo não encontrado ou não pode ser salvo.")
else:
    print("Conteúdo gravado com sucesso!")
    f.close()    
finally:
    print("Comandos nos blocos finally sempre são excutados!")