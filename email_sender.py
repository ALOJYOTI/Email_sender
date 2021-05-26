import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['from'] = 'A Mistry'
email['to'] = 'alojyotimistry1@gmail.com'
email['subject'] = 'just checking'
email.set_content('Hi, \n it is just a testing mail')

with smtplib.SMTP(host='smtp.gmail.com', port =587) as sender:
    sender.ehlo()
    sender.starttls()
    sender.login('a.mistry1000@gmail.com', '12345@Alo')
    sender.send_message(email)
    print("all done")