# Базы данных (БД)
# Реляционные - структурированные данные (таблицы, строки)
# Нереляционные - неструктурированные данные (ключ-значение, документы, графы, колоночные данные)
# Векторные - векторные данные (для поисковиков)
# СУБД (DBMS) - система управления базами данных
# SQL (Structured Query Language) - язык для общения с БД (получать, добавлять, удалять, обновлять данные)

# git rm --cached 'имя файла' - можно убрать файл после коммита из гита

# conn.execute() - SQL-запрос для работы с БД
# conn.commit() - сохраняем изменения в базе данных, нужно добавлять в каждой функции
# conn.close() - закрываем соединение с базой данных

import sqlite3

def create_tables():
    # команды принято писать caps'ом
    conn.execute('DROP TABLE IF EXISTS students') # удаляем таблицу если она существует, чтобы пересоздать с нуля
    # создаём таблицу, если её ещё нет и добавляем id к каждому элементу
    conn.execute("""
        CREATE TABLE If NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        city TEXT
        )
    """)

def add_student(name, age, city):
    conn.execute(
        "INSERT INTO students (name, age, city) VALUES (?, ?, ?)", # для безопасности принято передавать так, но можно и через f
        (name, age, city) # передаём значения вместо "?"
    )
    conn.commit()

def delete_student(student_id):
    # удаляем строку, где id = указанному
    conn.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,) # передаём id как параметр (обязательно запятая, так как это кортеж)
    )
    conn.commit()

if __name__ == '__main__': # код выполняется только если файл запущен напрямую
    conn = sqlite3.connect('database.db') # подключаемся или создаём БД

    create_tables()

    add_student('Aibek', 23, 'Bishkek')
    add_student('Nursultan', 20, 'Karakol')

    delete_student(1)

    conn.close()