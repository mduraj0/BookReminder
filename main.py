import email
from os import getenv
import sqlite3
from string import Template
from dotenv import load_dotenv
from borrowers import get_borrowers
from new_mail import DataBase
from send_mail import EmailSender, Credentials

load_dotenv()
connection = sqlite3.connect('DataBase.db')

port = getenv('PORT')
smtp_server = getenv('SMTP_SERVER')
user = getenv('USER')
password = getenv('PASSWORD')

credentials = Credentials(user, password)


def setup(connection):
    with DataBase(connection) as data_base:
        data_base.cursor.execute("""CREATE TABLE borrows(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT,
        book_title TEXT NOT NULL,
        book_return_at DATE,
        )""")


def send_reminder(borrower):
    template = Template("""Hi $name!\n
Do you remember that you have my book "$book_title"?
Give it back to me as soon as possible! The return date has passed $book_return_at! 
    
I am waiting :)
    """)

    text = template.substitute({
        'name': borrower.name,
        'book_title': borrower.book_title,
        'book_return_at': borrower.book_return_at
    })
    message = email.message_from_string(text)
    message.set_charset('utf-8')
    message['From'] = user
    message['To'] = user
    message['Subject'] = 'Overdue book'
    connection.send_mail(user, borrower.email, message)
    print(f'Sending mail to {borrower.email}')


if __name__ == '__main__':
    borrowers = get_borrowers(connection, '2022-12-24')
    with EmailSender(port, smtp_server, credentials) as connection:
        for borrower in borrowers:
            send_reminder(borrower)
