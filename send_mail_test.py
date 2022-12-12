from unittest.mock import patch
from send_mail import send_mail


@patch('smtplib.SMTP_SSL')
def test_send_mail(mock_smtp):
    send_mail()
    mock_smtp.assert_called()
    context = mock_smtp.return_value.__enter__.return_value
    context.login.assert_called()
    context.sendmail.assert_called_with('durajczykmichal@gmail.com',
                                        'durajczykmichal@gmail.com',
                                        'Sending first mail test')
