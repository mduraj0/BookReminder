from collections import namedtuple
from new_mail import DataBase

Entity = namedtuple('Entity', 'name email book_title book_return_at')


def get_borrowers(connection, book_return_at):
    entities = []

    with DataBase(connection) as data_base:
        data_base.cursor.execute("""SELECT
            name,
            email,
            book_title,
            book_return_at
        FROM borrows
        WHERE book_return_at < ?""", (book_return_at,))

        for name, email, book_title, book_return_at in data_base.cursor.fetchall():
            entities.append(Entity(name, email, book_title, book_return_at))

    return entities
