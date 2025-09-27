import sqlite3

def create_table():
    conn.execute('DROP TABLE IF EXISTS books')
    conn.execute('DROP TABLE IF EXISTS genres')
    conn.execute('DROP TABLE IF EXISTS books_archive')

    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        number_of_pages INTEGER,
        number_of_copies INTEGER,
        genre_id INTEGER,
        price INTEGER,
        deleted INTEGER DEFAULT 0
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS genres(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS books_archive (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        number_of_pages INTEGER,
        number_of_copies INTEGER,
        price INTEGER
        )
    """)

def insert_books(name, author, publication_year, number_of_pages, number_of_copies, genre_id, price):
    conn.execute(
        'INSERT INTO books (name, author, publication_year, number_of_pages, number_of_copies, genre_id, price) VALUES (?,?,?,?,?,?,?)',
        (name, author, publication_year, number_of_pages, number_of_copies, genre_id, price)
    )
    conn.commit()

def soft_delete(book_id):
    conn.execute(
        'UPDATE books SET deleted = 1 WHERE id = ?',
        (book_id,)
    )

    result = conn.execute(
        'SELECT name, author, publication_year, number_of_pages, number_of_copies, price FROM books WHERE id = ?',
        (book_id,)
    )
    book = result.fetchone()

    conn.execute(
        'INSERT INTO books_archive (name, author, publication_year, number_of_pages, number_of_copies, price) VALUES (?,?,?,?,?,?)',
        book
    )
    conn.commit()

def hard_delete(book_id):
    conn.execute(
        'DELETE FROM books WHERE id = ? AND deleted = 1',
        (book_id,)
    )
    conn.commit()

def add_genres(genres):
    conn.execute(
        'INSERT INTO genres (name) VALUES (?)',
        (genres,)
    )
    conn.commit()

def get_all_books():
    result = conn.execute('SELECT b.id, b.name, b.author, g.name FROM books AS b JOIN genres AS g ON b.genre_id = g.id')
    for row in result:
        print(row)
    return result.fetchall()

def filter_books_by_genre_name(genre: str):
    result = conn.execute(
        'SELECT b.name, b.author, g.name FROM books AS b JOIN genres AS g ON b.genre_id = g.id WHERE g.name = ?',
        (genre,)
    )
    for row in result:
        print(row)
    return result.fetchall()

def filter_genres_by_book_price(low: int, high: int):
    result = conn.execute(
        'SELECT g.name FROM books AS b JOIN genres AS g ON b.genre_id = g.id WHERE price BETWEEN ? AND ?',
        (low, high)
    )
    return result.fetchall()

if __name__ == '__main__':
    conn = sqlite3.connect('hw_db_2.db')

    create_table()

    add_genres('Romance')
    add_genres('Historical novel')
    add_genres('Philosophical novel')
    add_genres('Tragedy')
    add_genres('Adventure')

    insert_books(
        'Pride and Prejudice',
        'Jane Austen',
        1813,
        432,
        8,
        1,
        450
    )

    insert_books(
        'War and Peace',
        'Leo Tolstoy',
        1869,
        1225,
        7,
        2,
        1200
    )

    insert_books(
        'Crime and Punishment',
        'Fyodor Dostoevsky',
        1866,
        671,
        5,
        3,
        400
    )

    insert_books(
        'The Great Gatsby',
        'F. Scott Fitzgerald',
        1925,
        218,
        4,
        4,
        450
    )

    insert_books(
        'Jane Eyre',
        'Charlotte Brontë',
        1847,
        532,
        8,
        1,
        450
    )

    insert_books(
        'Wuthering Heights',
        'Emily Brontë',
        1847,
        416,
        4,
        4,
        400
    )

    insert_books(
        'Don Quixote',
        'Miguel de Cervantes',
        1605,
        863,
        5,
        5,
        600
    )

    insert_books(
        'The Brothers Karamazov',
        'Fyodor Dostoevsky',
        1880,
        824,
        8,
        3,
        800
    )

    insert_books(
        'Les Misérables',
        'Victor Hugo',
        1862,
        1463,
        6,
        2,
        900
    )
    print(filter_books_by_genre_name('Romance'))
    print(filter_genres_by_book_price(400, 500))
    print(get_all_books())
    soft_delete(1)
    hard_delete(1)

    conn.close()