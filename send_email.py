import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'thinkingwebco@gmail.com'
email['to'] = 'programmerblog.net@gmail.com'
email['subject'] = 'Welcome to Python!'
email.set_content('Wow! Hello world. Python Email')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('thinkingwebco@gmail.com', 'jqqeonvzhzbhfblr')
    smtp.send_message(email)
    print('The mail was sent!')


