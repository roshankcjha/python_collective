import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path  # similar to (os.path)
# SMTP-Simple Mail transfer protocol


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Name of the user from whom email is sent for this task'
email['to'] = 'receiver_email_id'
email['subject'] = 'Python mail test'


email.set_content(html.substitute({'name': 'TinTin'}), 'html')


with smtplib.SMTP(host='email_smtp', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sender_mail_id', 'sender_mail_password')
    smtp.send_message(email)
    print('Work done')

# Certain tasks to do before executing this task successfully:
# sender_mail_id,sender_mail_password,email_smtp,receiver_email_id should be replaced with actual mails
# You can use the SMTP of other mails .All you need to do is to search for them on the Net and understand their syntax of how to use them
