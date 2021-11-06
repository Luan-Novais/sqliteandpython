import os,sys
os.remove("escola.db") if os.path.exists("escola.db") else None

import sqlite3
con = sqlite3.connect('escola.db')
cur = con.cursor()
sql_create = 'create table cursos '\
    '(id integer primary key,   '\
    'titulo varchar(100), '\
    'categoria varchar(140))'
cur.execute(sql_create)

sql_insert = 'insert into cursos values (?,?,?)'

recset = [(100,'Ciencia de dados', 'Data Science'),
          (101,'Big Data Fundamentos', 'Big Data'),  
          (102,'Python Fundamentos', 'Analise de Dados')]

for rec in recset:
    cur.execute(sql_insert,rec)

sql_select = 'select * from cursos'


recset2 = (103,'Spark3','Big Data')
cur.execute(sql_insert,recset2)
con.commit()

cur.execute(sql_select)
dados = cur.fetchall()


for linha in dados:
    print('Curso id: %d, Título: %s, Categoria: %s \n' % linha)

con.close()