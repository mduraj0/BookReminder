import sqlite3
import pytest
from borrowers import get_borrowers


@pytest.fixture
def create_connection():
    connection = sqlite3.connect(':memory:')
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE borrows(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        book_title TEXT NOT NULL,
        book_return_at DATE,
        email TEXT)""")

    sample_data = [
        (1, 'Michal', 'Sample book', '2022-11-11', '123av@o2.pl'),
        (2, 'Robert', 'MySql', '2024-24-12', '123sadsa@wp.pl'),
        (3, 'Adam', 'Great book', '2019-12-15', 'asdvxzwq@o2.pl')
    ]

    cursor.executemany("""INSERT INTO borrows VALUES (?, ?, ?, ?, ?)""", sample_data)
    return connection


def test_get_borrowers(create_connection):
    users = get_borrowers(create_connection, '2023-10-20')
    assert users[0].name == 'Michal'
    assert users[1].name == 'Adam'
