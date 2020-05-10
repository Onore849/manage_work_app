import sqlite3
from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

sqlite_path = 'db/all_employee_table.db'

def get_db_connection():
    connection = sqlite3.connect(sqlite_path)
    connection.row_factory = sqlite3.Row
    return connection

# 従業員の一覧
@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    res = cursor.execute('SELECT * FROM employees_list')
    return render_template('index.html', employees_list=res.fetchall())

# 従業員の追加
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'GET':
        employee = {}
        return render_template('add_employee.html', employee=employee)
    else:
        connection = get_db_connection()
        cursor = connection.cursor()
        error = []

        if not request.form['name']:
            error.append('従業員名を追加してください')
        
        if error:
            employee = request.form.to_dict()
            # return render_template('edit.html', employee=employee, error_list=error)
            return render_template('add_employee.html', employee=employee, error_list=error)

        cursor.execute('INSERT INTO employees_list(name, comment) VALUES(?, ?)',
                        (request.form['name'],
                        request.form['comment'])
                        )
        
        connection.commit()
        return redirect(url_for('index'))
        
@app.route('/delete/<int:id>')
def delete(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute('DELETE FROM employees_list WHERE id=?',(id,))
    connection.commit()
    return redirect(url_for('index'))


@app.route('edit/<int:id>')
def edit(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    res = cursor.execute('SELECT * FROM days')
    return render_template('edit.html', date=res.fetchall())

if __name__ == '__main__':
    app.run(debug=True)