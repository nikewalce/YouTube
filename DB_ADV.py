import sqlite3 as sql

con = sql.connect('Bloggers.db') # создает файл с именем «test.db», если запустили впервые. То есть принимает на вход путь до файла с расширением .db

cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS `test` (`name` STRING, `surname` STRING)")

name = input("Name\n> ")
surname = input("Surname\n> ")

cur.execute(f"INSERT INTO `test` VALUES ('{name}', '{surname}')")#Добавление данных

#cur.execute("SELECT * FROM `test`") #Получение данных. И так как там отдаётся массив, то мы его перебираем, а после ещё и из кортежа данные берём.
#rows = cur.fetchall()#это что бы в переменную записалось всё, что пришло из БД.
#for row in rows:
#    print(row[0], row[1])

con.commit()#сохранение БД
cur.close()
