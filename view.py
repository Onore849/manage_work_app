import sqlite3
import datetime
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


@app.route('/edit<int:id>/month_list')
def edit(id):
    # connection = get_db_connection()
    # cursor = connection.cursor()
    # 今月を読み込む
    # today = datetime.datetime.now().month
    # res = cursor.execute('SELECT * FROM days WHERE rank={}'.format(today))
    # return render_template('edit.html', date=res.fetchall(), today_month=today)
    # res = cursor.execute('SELECT * FROM days')
    month_list = []
    for v in range(1, 13):
        month_list.append(v)
    return render_template('month_list.html', id=id, month_list=month_list)


@app.route('/edit<int:id>/month/<month_no>/')
def edit_month(month_no, id):
    connection = get_db_connection()
    cursor = connection.cursor()
    res = cursor.execute('SELECT * FROM days WHERE rank={}'.format(month_no))
    return render_template('month.html', date=res.fetchall(), month_no=month_no)


if __name__ == '__main__':
    app.run(debug=True)