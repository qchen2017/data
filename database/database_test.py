
import sqlite3
from sqlite3 import Error

#test2
# def sql_connection():
#     try:
#         con = sqlite3.connect(':memory:')
#         print("Connection is established: Database is created in memory")
#     except Error:
#         print(Error)
#     finally:
#         con.close()
# sql_connection()

# test3
# def sql_connection():
#     try:
#         con = sqlite3.connect('test.db')
#         return con
#     except Error:
#         print(Error)
#
# def sql_table(con):
#     cursorObj = con.cursor()
#     cursorObj.execute("CREATE TABLE employees(id integer PRIMARY KEY, name text, salary real, department text, position text, hireDate text)")
#     # employees (id, name, salary, department, position, hireDate)
#     con.commit()
#
# con = sql_connection()
# sql_table(con)

# test4:insert
con = sqlite3.connect('test.db')
cursorObj = con.cursor()

# cursorObj.execute("INSERT INTO employees VALUES(1, 'John', 700, 'HR', 'Manager', '2017-01-04')")

# def sql_insert(con, entities):
#     cursorObj = con.cursor()
#     cursorObj.execute(
#         'INSERT INTO employees(id, name, salary, department, position, hireDate) VALUES(?, ?, ?, ?, ?, ?)', entities)
#     con.commit()
#
# entities = (2, 'Andgrew', 800, 'IT', 'Tech', '2018-02-07')
# sql_insert(con, entities)

# test4:update
# def sql_update(con):
#     cursorObj = con.cursor()
#     cursorObj.execute('UPDATE employees SET name = "Rogers" where id = 2')
#     con.commit()
# sql_update(con)

# test5: select
# def sql_fetch(con):
#     cursorObj = con.cursor()
#     # cursorObj.execute('SELECT * FROM employees')
#     # print(cursorObj.execute('SELECT id, name FROM employees'))
#     cursorObj.execute('SELECT id, name FROM employees WHERE salary > 700.0')
#     rows = cursorObj.fetchall()
#     for row in rows:
#         print(row)
#
# sql_fetch(con)

# test6: rowcount
# print(cursorObj.execute('SELECT * FROM employees').rowcount) # wrong:不正确的表达方式
# cursorObj.execute('SELECT * FROM employees')
# rows = cursorObj.fetchall()
# print(len (rows))

# test7: list all tables获取所有表格
# def sql_fetch(con):
#     cursorObj = con.cursor()
#     cursorObj.execute('SELECT name from sqlite_master where type= "table"')
#     print(cursorObj.fetchall())
#
# sql_fetch(con)
#另一种方式
cursorObj.execute('SELECT name from sqlite_master WHERE type = "table" AND name = "employees"')
print(cursorObj.fetchall())

# test8: Check if a table exists or not
# def sql_fetch(con):
#     cursorObj = con.cursor()
#     cursorObj.execute('create table if not exists projects(id integer, name text)')
#     con.commit()
#
# sql_fetch(con)
# cursorObj.execute('drop table if exists projects') #删除表格







