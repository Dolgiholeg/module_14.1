import sqlite3

connection = sqlite3.connect("not_telegram.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)   
''')
cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

# Создание таблицы Users
# Заполнение её 10 записями
# for i in range(1, 11):
#     n = 10
#     cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
#                    (f"User{i}", f"example{i}x@gmail.com", f"{i * n}", "1000"))

# Обновляю balance у каждой 2ой записи начиная с 1ой на 500:
# for i in range(1, 11):
#     if i % 2 == 0:
#         cursor.execute("UPDATE Users SET balance = ? WHERE username = ?", ("500", f"User{i}"))

# Удаляю каждую 3ую запись в таблице начиная с 1ой:
# for i in range(1, 11, 3):
#      cursor.execute("DELETE FROM Users WHERE username = ?", (f'User{i}',))

# Делаю выборку всех записей при помощи fetchall(), где возраст не равен 60 и вывожу их в консоль в следующем формате (без id):
# Имя: <username> | Почта: <email> | Возраст: <age> | Баланс: <balance>
cursor.execute("SELECT username, email, age, balance FROM Users WHERE AGE != ?", (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}')


connection.commit()
connection.close()

