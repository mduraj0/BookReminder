from collections import namedtuple
import smtplib, ssl

Credentials = namedtuple('Credentials', 'username password')


class EmailSender:
    def __init__(self, port, smtp_server, credentials):
        self.port = port
        self.smtp_server = smtp_server
        self.connection = None
        self.credentials = credentials

    def __enter__(self):
        context = ssl.create_default_context()
        self.connection = smtplib.SMTP_SSL(self.smtp_server, self.port, context=context)
        self.connection.login(self.credentials.username, self.credentials.password)

        return self

    def send_mail(self, user, receiver, message):
        self.connection.sendmail(user, receiver, message.as_string())

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()
