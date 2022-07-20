def send_mail_preorder(message, user):

    import smtplib
    from email.mime.text import MIMEText
    from email.header import Header

    smtp_host = 'smtp.mail.ru'

    login = 'nikitad5890@mail.ru'
    password = 'qIdYnfevtG5c8c3Vzzr4'
    recipients_emails = ['nikitad5890@gmail.com', "artem1564726@gmail.com"]

    msg = MIMEText('Пользователь '+user+' оставил предзаказ:\n'+message, 'plain', 'utf-8')
    msg['Subject'] = Header('Предзаказ от '+user, 'utf-8')
    msg['From'] = login
    msg['To'] = ", ".join(recipients_emails)

    s = smtplib.SMTP(smtp_host, 587, timeout=10)
    s.set_debuglevel(1)
    try:
        s.starttls()
        s.login(login, password)
        s.sendmail(msg['From'], recipients_emails, msg.as_string())
    finally:
        s.quit()