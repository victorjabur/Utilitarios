#! /usr/bin/python

import os, time, tarfile, sys
from datetime import datetime

diretorio = '/home/victor/teste'
destinoTarGz = '/home/victor/teste/backup.tar.gz'
dataHora = '26/01/2012-12:00:00'

dataHoraParam = datetime.strptime(dataHora, '%d/%m/%Y-%H:%M:%S')
dataHoraParamTimestamp = time.mktime(dataHoraParam.timetuple())

listaElementosCopiar = []

def criarTarGz():
    t = tarfile.open(name = destinoTarGz, mode = 'w:gz')
    for elemento in listaElementosCopiar:
        t.add(elemento, recursive=False)
    t.close()

def processaElemento(elemento):
    data_modificacao = os.path.getmtime(elemento)
    if data_modificacao > dataHoraParamTimestamp:
        listaElementosCopiar.append(elemento)
    return elemento

def itera(item):
    for elemento in os.listdir(item):
        elemento = os.path.join(item,elemento)
        if os.path.isdir(elemento):
            itera(processaElemento(elemento))
        else:
            processaElemento(elemento)

if __name__ == '__main__':
    itera(diretorio)
    criarTarGz()