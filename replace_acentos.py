#! /usr/bin/python
# -*- coding: iso-8859-1 -*-

import sys,os
from unicodedata import normalize

pasta_origem = sys.argv[1]

def retirar_acento(str):
    return normalize('NFKD', str.decode(sys.getfilesystemencoding())).encode('ASCII','ignore')

def substituir(str):
    str = str.replace(' - ','-')
    str = str.replace(' ','_')
    return str

def renomear(item):
    caminho_novo = substituir(retirar_acento(item))
    os.rename(item, caminho_novo)
    return caminho_novo

def itera(item):
    if os.path.isdir(item):
        for elemento in os.listdir(item):
            elemento = os.path.join(item,elemento)
            if os.path.isdir(elemento):
                itera(renomear(elemento))
            else:
                renomear(elemento)
    else:
        renomear(item)

if __name__ == '__main__':
    itera(pasta_origem)

