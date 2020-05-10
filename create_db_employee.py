import sqlite3
import calendar
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


try:
    cur.execute('DROP TABLE IF EXISTS days')
    for v in range(1,13):
        cur.execute('CREATE TABLE IF NOT EXISTS days (dates TEXT , weekdays TEXT, str_time TEXT, end_time TEXT, status TEXT, rank TEXT)')
        
        c = calendar.Calendar()
        month = c.itermonthdates(2019, v)

        for i in month:
            if i.month == v:
                weekday = ['月', '火', '水', '木', '金', '土', '日']
                day_name = weekday[i.weekday()]
                day = f'{i: %m月%d日}'
                cur.execute('INSERT INTO days(dates, weekdays, rank) VALUES (?, ?, ?)', (day, day_name, v))
        
                connection.commit()

except sqlite3.Error as e:
    print('sqlite3.Error has occurred', e.args[0])

cur.execute('SELECT * FROM days')
print(cur.fetchall())
connection.close()

