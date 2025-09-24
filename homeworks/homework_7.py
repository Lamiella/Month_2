import sqlite3

def create_table():
    conn.execute('DROP TABLE IF EXISTS books')
    conn.execute('DROP TABLE IF EXISTS books_archive')

    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER,
        deleted INTEGER DEFAULT 0
        )
    """)

    conn.execute("""
        CREATE TABLE IF NOT EXISTS books_archive (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        author TEXT,
        publication_year INTEGER,
        genre TEXT,
        number_of_pages INTEGER,
        number_of_copies INTEGER
        )
    """)
    conn.commit()

def insert_books(name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute(
        'INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES (?,?,?,?,?,?)',
        (name, author, publication_year, genre, number_of_pages, number_of_copies)
    )
    conn.commit()

def soft_delete(book_id):
    conn.execute(
        'UPDATE books SET deleted = 1 WHERE id = ?',
        (book_id,)
    )

    result = conn.execute(
        'SELECT id, name, author, publication_year, genre, number_of_pages, number_of_copies FROM books WHERE id = ?',
        (book_id,)
    )
    book = result.fetchone()

    conn.execute(
        'INSERT INTO books_archive (id, name, author, publication_year, genre, number_of_pages, number_of_copies) VALUES (?, ?, ?, ?, ?, ?, ?)',
        book
    )
    conn.commit()

def hard_delete(book_id):
    conn.execute(
        'DELETE FROM books WHERE id = ? AND deleted = 1',
        (book_id,)
    )
    conn.commit()


if __name__ == '__main__':
    conn = sqlite3.connect('hw_db.db')

    create_table()

    insert_books(
        '1984',
        'George Orwell',
        1949,
        'Dystopian political fiction social science fiction',
        328,
        7
    )

    insert_books(
        'Pride and Prejudice',
        'Jane Austen',
        1813,
        'Romance, Satire',
        432,
        8
    )

    insert_books(
        'Moby-Dick',
        'Herman Melville',
        1851,
        'Adventure, Epic, Maritime',
        635,
        4
    )

    insert_books(
        'War and Peace',
        'Leo Tolstoy',
        1869,
        'Historical novel, Philosophical fiction',
        1225,
        7
    )

    insert_books(
        'Crime and Punishment',
        'Fyodor Dostoevsky',
        1866,
        'Psychological fiction, Philosophical novel',
        671,
        5
    )

    insert_books(
        'The Great Gatsby',
        'F. Scott Fitzgerald',
        1925,
        'Tragedy, Historical',
        218,
        4
    )

    insert_books(
        'Jane Eyre',
        'Charlotte Brontë',
        1847,
        'Romance, Gothic fiction',
        532,
        8
    )

    insert_books(
        'Wuthering Heights',
        'Emily Brontë',
        1847,
        'Tragedy, Gothic fiction',
        416,
        8
    )

    insert_books(
        'The Catcher in the Rye',
        'J.D. Salinger',
        1951,
        'Coming-of-age, Realism',
        277,
        6
    )

    insert_books(
        'Brave New World',
        'Aldous Huxley',
        1932,
        'Science fiction, Dystopian',
        311,
        4
    )

    insert_books(
        'Don Quixote',
        'Miguel de Cervantes',
        1605,
        'Satire, Adventure',
        863,
        5
    )

    insert_books(
        'The Brothers Karamazov',
        'Fyodor Dostoevsky',
        1880,
        'Philosophical novel, Psychological fiction',
        824,
        8
    )

    insert_books(
        'Les Misérables',
        'Victor Hugo',
        1862,
        'Historical novel, Drama',
        1463,
        6
    )

    insert_books(
        'Anna Karenina',
        'Leo Tolstoy',
        1877,
        'Realist novel, Romance',
        864,
        5
    )

    insert_books(
        'To Kill a Mockingbird',
        'Harper Lee',
        1960,
        'Southern Gothic, Bildungsroman',
        281,
        4
    )

    soft_delete(1)
    hard_delete(1)

    conn.close()