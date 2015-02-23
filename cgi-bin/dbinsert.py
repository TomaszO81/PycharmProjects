#!/usr/bin/python
import sqlite3 as db

conn = db.connect('test.db')
cursor = conn.cursor()
cursor.execute("insert into films (title, year, director) values ('Annie Hall', '1977','Woody Allen')")
cursor.execute('insert into films (title, year, director) values ("The Godfather", "1972", "Francis Ford Coppola")')
conn.commit()
conn.close()