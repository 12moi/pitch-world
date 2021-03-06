

from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject, template, to, **kwargs):
    sender_mail = 'pitchesapp@gmail.com'

    email = Message(subject, sender = sender_mail, recipients = [to])
    email_body = render_template(template + '.txt', **kwargs)
    email.html = render_template(template + '.html', **kwargs)
    # mail.send(email)