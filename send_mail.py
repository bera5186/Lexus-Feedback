import smtplib
from email.mime.text import MIMEText

def send_mail(customer, dealer, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '53ee80a077ba51'
    password = 'c63dc0938f1de6'
    message = f'<h3>New feedback Submission</h3><ul><li>Customer : {customer}</li></ul><ul><li>Dealer : {dealer}</li></ul><ul><li>Rating : {rating}</li></ul><ul><li>Comments : {comments}</li></ul>'

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
