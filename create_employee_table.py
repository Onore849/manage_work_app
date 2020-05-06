import sqlite3
sqlite_path = 'db/all_employee_table.db'
connection = sqlite3.connect(sqlite_path)
cur = connection.cursor()

try:
    # テーブルの作成
    cur.execute('DROP TABLE IF EXISTS employees_list')
    cur.execute('CREATE TABLE IF NOT EXISTS employees_list(id INTEGER PRIMARY KEY, name TEXT, comment TEXT)')

    cur.execute('INSERT INTO employees_list VALUES (?, ?, ?)', (1, '野澤', 'testです'))
    
except sqlite3.Error as e:
    print('sqlite3.ERROR.occured', e.args[0])


# cur.execute('SELECT * FROM employees_list')
# print(cur.fetchall())
connection.close()

