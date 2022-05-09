import smtplib
import ssl
import time
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(password, from_email, to_email, f):
    t = time.time()
    sender_address = from_email
    receiver_address = to_email
    message = MIMEMultipart("alternative")
    message['from'] = sender_address
    message['to'] = receiver_address
    message['subject'] = f'art-{t}'

    mail_content = f'''Hello {message['to']},
    the email contains the results of the experiment as an attachment.
    Best,
    {message['from']}'''
    
    message.attach(MIMEText(mail_content, 'plain'))
    
    try:
        with open(f, 'rb') as attachment:
            p = MIMEApplication(attachment.read(), _subtype='pdf')
            p.add_header('Content-Disposition', 'attachment', filename=f'art-{t}.pdf')
            message.attach(p)

    except Exception as e:
        print(str(e))

    make_context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=make_context) as server:

        server.login(sender_address, password)
        server.sendmail(sender_address, receiver_address, message.as_string())