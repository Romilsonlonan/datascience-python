#!/usr/bin/python

import os, sys

# Primeiro vá para o diretório "/var/www/html" 
os.chdir("/var/www/html" )

# Imprimir diretório de trabalho atual
print ("Current working dir : %s" % os.getcwd())

# Agora abra um diretório"/tmp"
fd = os.open( "/tmp", os.O_RDONLY )

# Use o método os.fchdir() para alterar o diretório
os.fchdir(fd)

# Imprimir diretório de trabalho atual
print ("Current working dir : %s" % os.getcwd())

# Feche o diretório aberto.
os.close( fd )