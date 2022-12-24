import smtplib
from email.message import EmailMessage
from pathlib import Path
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders

html_content = Path('template.html').read_text()

email = MIMEMultipart()
email['from'] = 'thinkingwebco@gmail.com'
email['to'] = 'programmerblog.net@gmail.com'
email['subject'] = 'Welcome to Python email using SMTPLib!'
email.attach(MIMEText(html_content, 'html'))
filename = 'sample.pdf'

with open(filename, 'rb') as attachment:
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f'attachment;filename={filename}')
    email.attach(part)
    
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login('thinkingwebco@gmail.com', 'jqqeonvzhzbhfblr')

    if(smtp.send_message(email)):
        print('The mail with attachment was sent sucessfully!')
    else:
        print('The mail with attachment was not sent.')

