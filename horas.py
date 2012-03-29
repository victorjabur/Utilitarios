#! /usr/bin/python
# -*- coding: iso-8859-1 -*-
import requests, lancto
from datetime import datetime

def login():
    usuario = 'user'
    senha = 'pass'
    post_login = {'login':'login', 'username':usuario, 'password':senha, 'login.x':'13', 'login.y':'12'}
    r = requests.post('http://www.dscon.com.br/pmo/index.php', post_login)
    return r

def lancar(r, data, hora_inicio, hora_fim, descricao):
    id_criador = '68'
    task_id = '3604'
    task_name = unicode('ALOCAÇÃO', 'iso-8859-1')
    descricao = unicode(descricao, 'iso-8859-1')
    task_log_id = ''

    total_horas = (datetime.strptime(hora_fim, '%H:%M') - datetime.strptime(hora_inicio, '%H:%M')).seconds / 3600.00
    post_lancto = {'task_log_id':task_log_id, 'task_log_creator':id_criador, 'task_log_hours':total_horas, 'task_end_date':data+' '+hora_inicio+':00', 'task_log_date':data+' '+hora_inicio+':00', 'task_log_task':task_id, 'task_log_name':task_name,'start_time':hora_inicio, 'end_time':hora_fim, 'task_log_description':descricao, 'dosql':'do_updatetask'}
    requests.post('http://www.dscon.com.br/pmo/index.php?m=tasks&a=view&task_id='+task_id, post_lancto, cookies=r.cookies)

r = login()
lista_lancto = []
lista_lancto.append(lancto.lancto('2012-03-01', '11:00', '11:50', 'contestacao 11g'))


for lcto in lista_lancto:
    lancar(r, lcto.data, lcto.hora_inicio, lcto.hora_fim, lcto.descricao)