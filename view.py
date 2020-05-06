import sqlite3
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

sqlite_path = 'db/all_employee_table.db'

def get_db_connection():
    connection = sqlite3.connect(sqlite_path)
    connection.row_factory = sqlite3.Row
    return connection

@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    res = cursor.ececute('SELECT * FROM employees_list')
    return render_template('index.html', employees_list=res.fetchall())

