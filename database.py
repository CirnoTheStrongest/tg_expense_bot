import sqlite3
from datetime import datetime

DB_PATH = "expenses.db"

# Функция подключения к БД
def connect_db():
    return sqlite3.connect(DB_PATH)

# Создаём таблицу расходов, если её нет
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            amount REAL,
            category TEXT,
            date TEXT
        )
    ''')

    conn.commit()
    conn.close()

# Функция для добавления расхода
def add_expense(user_id, amount, category="Прочее"):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO expenses (user_id, amount, category, date)
        VALUES (?, ?, ?, ?)
    ''', (user_id, amount, category, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))

    conn.commit()
    conn.close()

# Функция для получения суммы расходов за сегодня
def get_today_expenses(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")
    cursor.execute('''
        SELECT SUM(amount) FROM expenses
        WHERE user_id = ? AND date LIKE ?
    ''', (user_id, today + "%"))

    total = cursor.fetchone()[0]
    conn.close()
    return total if total else 0.0

# Функция для получения всех расходов за сегодня с их ID
def get_today_expenses_list(user_id):
    conn = connect_db()
    cursor = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")
    cursor.execute('''
        SELECT id, amount, category, date FROM expenses
        WHERE user_id = ? AND date LIKE ?
    ''', (user_id, today + "%"))

    expenses = cursor.fetchall()
    conn.close()
    return expenses

# Функция для удаления расхода по ID
def delete_expense(expense_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM expenses WHERE id = ?
    ''', (expense_id,))

    conn.commit()
    conn.close()

