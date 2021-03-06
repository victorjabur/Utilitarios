#! /usr/bin/python
# -*- coding: utf-8 -*-

import urllib,httplib
from datetime import datetime

class Horas:

    def __init__(self):
        self.usuario = 'user'
        self.senha = 'senha'
        self.projetos = {1 : Projeto('3604', 'ALOCAÇÃO', 'Projeto Contestacao'),
                         2 : Projeto('4058', 'DESENVOLVIMENTO', 'Projeto Sao Paulo Caminhoneiro'),
                         3 : Projeto('1307','Manutenção Evolutiva','Call Center Manutencao')}

    def login(self):
        body = {'login':'login', 'username':self.usuario, 'password':self.senha, 'login.x':'13', 'login.y':'12'}
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        self.conn = httplib.HTTPConnection('dscon.com.br:80')
        self.conn.request('POST', '/pmo/index.php', urllib.urlencode(body), headers)
        response = self.conn.getresponse()
        return {'Content-type': 'application/x-www-form-urlencoded', 'Cookie': response.getheader('set-cookie')}

    def lancar(self, r, projeto, data, hora_inicio, hora_fim, descricao):
        id_criador = '68'
        task_id = projeto.task_id
        task_name = unicode(projeto.descricao, 'utf-8').encode('utf-8')
        descricao = unicode(descricao, 'utf-8').encode('utf-8')
        task_log_id = ''
        total_horas = (datetime.strptime(hora_fim, '%H:%M') - datetime.strptime(hora_inicio, '%H:%M')).seconds / 3600.00
        body = {'task_log_id':task_log_id, 'task_log_creator':id_criador, 'task_log_hours':total_horas, 'task_end_date':data+' '+hora_inicio+':00', 'task_log_date':data+' '+hora_inicio+':00', 'task_log_task':task_id, 'task_log_name':task_name,'start_time':hora_inicio, 'end_time':hora_fim, 'task_log_description':descricao, 'dosql':'do_updatetask'}
        self.conn.request('POST','/pmo/index.php?m=tasks&a=view&task_id='+task_id, urllib.urlencode(body), r)
        response = self.conn.getresponse()

    def main(self):
        r = self.login()
        lista_lancto = []
        lista_lancto.append(Lancto(1, '2012-05-01', '09:00', '10:00', 'Contestação - reteste dos fluxos da contetação.'))
        # Colocar os lancamentos aqui ...

        for lcto in lista_lancto:
            self.lancar(r, self.projetos.get(lcto.codigo_projeto), lcto.data, lcto.hora_inicio, lcto.hora_fim, lcto.descricao)

class Lancto:
    def __init__(self, codigo_projeto, data, hora_inicio, hora_fim, descricao):
        self.codigo_projeto = codigo_projeto
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.descricao = descricao

class Projeto:
    def __init__(self, task_id, descricao, complemento):
        self.task_id = task_id
        self.descricao = descricao
        self.complemento = complemento

if __name__ == "__main__":
    horas = Horas()
    horas.main()
    print 'Horas lançadas com sucesso :-)'