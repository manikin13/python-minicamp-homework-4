from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect('database.db')
print ('database Opened sucessfully!')

connection.execute('CREATE TABLE IF NOT EXISTS movies (name TEXT, mFormat TEXT, genre TEXT)')
print ('table created sucessfully!')
connection.close()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/dataentry')
def dataentry():
    return render_template('movie.html')


@app.route('/movie', methods = ['POST'])
def movie():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    name = request.form['name']
    mFormat = request.form['mFormat']
    genre = request.form['genre']
    try:
        cursor.execute('INSERT INTO movies(name, mFormat, genre) VALUES (?, ?, ?)', (name, mFormat, genre))
        connection.commit()
        message = 'Record successfully updated!'
    except:
        connection.rollback()
        message = 'Error in updating database!'
    finally:
        return render_template('result.html', message = message)
        connection.close()


@app.route('/movies')
def movies():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute('SELECT * from movies')
    rows = cursor.fetchall()
    connection.close()
    return render_template('list.html', rows = rows)
