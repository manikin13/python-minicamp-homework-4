import sqlite3
connection = sqlite3.connect('database.db')
print ('Opened database sucessfully!')
connection.execute('CREATE TABLE movies (name TEXT, mFormat TEXT, genre TEXT)')
print ('Table created cucessfully!')
connection.close()
