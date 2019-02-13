#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import psycopg2

DBNAME = "news"


# Consulta no Banco de Dados
def buscar_dados(consulta):
    """Buscando dados do Banco de Dados"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(consulta)
    resultado = c.fetchall()
    db.close()
    return resultado


# Retorna valores do banco de dados, referentes aos 3 artigos
#  mais populares
def artigos_populares():
    query_artigos_populares = "select title, views " \
                              "from artigos_populares limit 3"
    resultado = buscar_dados(query_artigos_populares)
    print ('Os três artigos mais populares de todos os tempos são: ')
    print ('')
    for title, views in resultado:
        print ('"{title}" -- {views} Visualizações'
               .format(title=title, views=views))


# Retorna valores do banco de dados, referentes aos autores mais populares
def autores_populares():
    query_autores_populares = "select name, views from autores_populares"
    resultado = buscar_dados(query_autores_populares)
    print('Os autores de artigos mais populares de todos os tempos são: ')
    print ('')
    for name, views in resultado:
        print ('"{name}" -- {views} Visualizações'
               .format(name=name, views=views))


# Retorna valores do banco de dados por data,
#  referentes a eventuais erros de acessos
def log_erros():
    query_log_erros = "select data, percentual_erros from log_erros " \
                      "where percentual_erros > 1"
    resultado = buscar_dados(query_log_erros)
    print ('Os dias em que mais de 1% das requisições '
           'resultaram em erros foram: ')
    print ('')
    for data, percentual_erros in resultado:
        print ('"{data}" -- {percentual_erros}'
               .format(data=data, percentual_erros=percentual_erros))


# Imprime os resultados
if __name__ == '__main__':
    artigos_populares()
    print ('')
    autores_populares()
    print ('')
    log_erros()
