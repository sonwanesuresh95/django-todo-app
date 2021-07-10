import sqlite3

connection = sqlite3.connect('db.sqlite3')

cursor = connection.cursor()

records = cursor.execute('select * from todoapp_task')

print(records)