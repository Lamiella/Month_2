# Базы данных (БД)
# Реляционные - структурированные данные (таблицы, строки, колонки)
# Нереляционные - неструктурированные данные (ключ-значение, документы, графы, колоночные данные)
# Векторные - векторные данные (для поисковиков)
# СУБД (DBMS) - система управления базами данных
# SQL (Structured Query Language) - язык для общения с БД (получать, добавлять, удалять, обновлять данные)
# Primary key (первичный ключ) - для идентификации записи в таблице
# Foreign key (внешний ключ) - для связи таблиц

# git rm --cached 'имя файла' - можно убрать файл после коммита из гита

# conn.execute() - SQL-запрос для работы с БД
# conn.commit() - сохраняем изменения в базе данных, нужно добавлять в каждой функции (DELETE, UPDATE, INSERT)
# conn.close() - закрываем соединение с базой данных

import sqlite3

def create_tables():
    """Функция для создания таблиц"""
    # команды принято писать caps'ом
    conn.execute('DROP TABLE IF EXISTS students') # удаляем таблицу если она существует, чтобы пересоздать с нуля
    conn.execute('DROP TABLE IF EXISTS departments')

    # создаём таблицу, если её ещё нет и добавляем id к каждому элементу
    conn.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE If NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            age INTEGER,
            city TEXT,
            department_id INTEGER,
            FOREIGN KEY(department_id) REFERENCES departments(id)
        )
    """)


def add_student(name: str, age: int, city: str, department_id: int):
    """Функция для добавления строк"""
    conn.execute(
        "INSERT INTO students (name, age, city, department_id) VALUES (?, ?, ?, ?)", # для безопасности принято передавать так, но можно и через f
        (name, age, city, department_id) # передаём значения вместо "?"
    )
    conn.commit()

def delete_student(student_id: int):
    """Функция для удаления строк"""
    # удаляем строку, где id = указанному
    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,) # передаём id как параметр (обязательно запятая, так как это кортеж)
    )
    conn.commit()

def get_some_students():
    """Функция для вызова строк"""
    result = conn.execute('SELECT name, age FROM students ORDER BY age LIMIT 2')
    return result.fetchall()

"""Другой вариант вызова конкретного кол-ва строк"""
# def get_all_students():
#     result = conn.execute('SELECT name, age FROM students')
#     return result.fetchmany(2)

def get_all_students():
    result = conn.execute('SELECT s.name, d.name FROM students AS s JOIN departments AS d ON s.department_id = d.id')
    return result.fetchall()

def get_student(name: str):
    result = conn.execute('SELECT * FROM students WHERE name = ?', (name,))
    return result.fetchall()

def update_student_name(new_name: str, student_id: int):
    conn.execute('UPDATE students SET name = ? WHERE id = ?', (new_name, student_id))
    conn.commit()

def add_department(name: str):
    conn.execute('INSERT INTO departments (name) VALUES (?)', (name,))

if __name__ == '__main__': # код выполняется только если файл запущен напрямую
    conn = sqlite3.connect('database.db') # подключаемся или создаём БД

    create_tables()

    add_department('Backend')
    add_department('Frontend')

    add_student('Aibek', 23, 'Bishkek', 1)
    add_student('Nursultan', 20, 'Karakol', 2)
    add_student('Alina', 21, 'Osh', 1)
    add_student('Tilek', 25, 'Bishkek', 2)
    add_student("Aidana", 20, "Karakol", 1)
    add_student("Bakyt", 24, "Osh", 1)
    add_student("Gulnara", 18, "Bishkek", 1)
    add_student("Tilek", 23, "Karakol", 1)

    print(get_some_students())
    print(get_all_students())
    print(get_student('Aibek'))

    delete_student(1)

    update_student_name('Alena', 3)

    conn.close()