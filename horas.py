#! /usr/bin/python
# -*- coding: iso-8859-1 -*-
import requests, lancto
from datetime import datetime

def login():
    usuario = 'user'
    senha = 'senha'
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
lista_lancto.append(lancto.lancto('2012-01-02', '10:25', '12:30', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-02', '14:00', '19:10', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-03', '11:50', '13:10', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-03', '13:50', '20:40', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-04', '12:50', '21:00', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-05', '10:00', '12:20', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-05', '13:25', '21:45', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-06', '09:30', '12:20', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-06', '14:15', '18:55', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-07', '09:00', '13:00', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-07', '14:00', '18:00', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-09', '09:30', '13:00', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-09', '14:00', '19:00', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-10', '11:30', '13:00', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-10', '14:00', '18:00', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-11', '12:00', '19:45', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-12', '10:30', '12:40', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-12', '13:40', '19:20', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-13', '09:30', '12:10', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-13', '14:10', '19:15', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-16', '11:30', '20:30', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-17', '08:00', '13:00', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-17', '14:00', '20:00', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-18', '08:30', '13:00', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-18', '13:50', '18:30', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-19', '10:30', '13:00', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-19', '14:00', '22:00', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-20', '09:40', '12:45', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-20', '13:20', '23:10', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-23', '09:30', '12:20', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-23', '13:20', '19:15', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-24', '09:00', '12:25', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-24', '13:25', '19:00', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-26', '09:30', '12:30', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-26', '13:30', '19:00', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-27', '11:30', '13:30', 'contestacao 11g'))
lista_lancto.append(lancto.lancto('2012-01-27', '14:30', '21:00', 'contestacao 11g'))

for lcto in lista_lancto:
    lancar(r, lcto.data, lcto.hora_inicio, lcto.hora_fim, lcto.descricao)