#! /usr/bin/python
# -*- coding: iso-8859-1 -*-

import os, fileinput, argparse

parser = argparse.ArgumentParser(description='Rename diretorios e arquivos do svn')
parser.add_argument('-diretorio')
parser.add_argument('-de')
parser.add_argument('-para')
results = parser.parse_args()

diretorio_inicial = results.diretorio
string_de = results.de
string_para = results.para

def renomear_conteudo_arquivo(item):
    for line in fileinput.input(item, inplace = 1):
        print line.replace(string_de, string_para),

def renomear_dir_ou_file(item):
    nome_novo = item.replace(string_de, string_para)
    os.rename(item, nome_novo)
    if os.path.isfile(nome_novo):
        renomear_conteudo_arquivo(nome_novo)
    return nome_novo

def itera(item):
    for elemento in os.listdir(item):
        elemento = os.path.join(item,elemento)
        if elemento.find('.svn') == -1 and elemento.find('CVS') == -1:
            if os.path.isdir(elemento):
                itera(renomear_dir_ou_file(elemento))
            else:
                renomear_dir_ou_file(elemento)

if __name__ == '__main__':
    itera(diretorio_inicial)
