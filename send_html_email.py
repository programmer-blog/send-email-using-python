import smtplib
from email.message import EmailMessage
from pathlib import Path

html_content = Path('template.html').read_text()

email = EmailMessage()
email['from'] = 'thinkingwebco@gmail.com'
email['to'] = 'programmerblog.net@gmail.com'
email['subject'] = 'Welcome to Python!'
email.set_content(html_content, 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('thinkingwebco@gmail.com', 'jqqeonvzhzbhfblr')
    smtp.send_message(email)

    print('The mail was sent!')


