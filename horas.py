#! /usr/bin/python
# -*- coding: utf-8 -*-
import requests, lancto
from datetime import datetime

class Horas:

    def login(self):
        usuario = 'user'
        senha = 'senha'
        post_login = {'login':'login', 'username':usuario, 'password':senha, 'login.x':'13', 'login.y':'12'}
        r = requests.post('http://www.dscon.com.br/pmo/index.php', post_login)
        return r

    def lancar(self, r, data, hora_inicio, hora_fim, descricao):
        id_criador = '68'
        task_id = '3604'
        task_name = unicode('ALOCAÇÃO', 'utf-8')
        descricao = unicode(descricao, 'utf-8')
        task_log_id = ''

        total_horas = (datetime.strptime(hora_fim, '%H:%M') - datetime.strptime(hora_inicio, '%H:%M')).seconds / 3600.00
        post_lancto = {'task_log_id':task_log_id, 'task_log_creator':id_criador, 'task_log_hours':total_horas, 'task_end_date':data+' '+hora_inicio+':00', 'task_log_date':data+' '+hora_inicio+':00', 'task_log_task':task_id, 'task_log_name':task_name,'start_time':hora_inicio, 'end_time':hora_fim, 'task_log_description':descricao, 'dosql':'do_updatetask'}
        requests.post('http://www.dscon.com.br/pmo/index.php?m=tasks&a=view&task_id='+task_id, post_lancto, cookies=r.cookies)

    def main(self):
        r = self.login()
        lista_lancto = []
        lista_lancto.append(lancto.lancto('2012-03-12', '10:30', '12:30', 'contestacao 11g'))
        # Colocar os lancamentos aqui ...

        for lcto in lista_lancto:
            self.lancar(r, lcto.data, lcto.hora_inicio, lcto.hora_fim, lcto.descricao)

class Lancto:
    def __init__(self, data, hora_inicio, hora_fim, descricao):
        self.data = data
        self.hora_inicio = hora_inicio
        self.hora_fim = hora_fim
        self.descricao = descricao

if __name__ == "__main__":
    horas = Horas()
    horas.main()