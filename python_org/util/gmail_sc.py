import imaplib

IMAPSERVER = 'imap.gmail.com'
USER = 'avalanche1492@gmail.com'
PASSWORD = 'sep022014'

try:
    mail = imaplib.IMAP4_SSL(IMAPSERVER, 993)
    mail.login(USER, PASSWORD)
    status, messages = mail.select("INBOX")

    new_mail = mail.search(None, 'unseen')[1][0]
    new_mail = new_mail.decode("utf-8")

    print(len(new_mail))

    mail.close()
    mail.logout()
    #
    # return_code, mail_ids = mail.search(None, '*')
    # count = len(mail_ids[0].split(" "))
except:
    print('unable to connect')
