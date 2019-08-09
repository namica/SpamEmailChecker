import imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com',993)
M.login("youremail@gmail.com", "yourpassword")
M.select('Inbox')
typ, data = M.search(None, 'ALL')
for num in data[0].split():
    typ, data = M.fetch(num, '(RFC822)')
    msg= str(data[0][1]).split("\\r\\n")
    for m in msg:
        print(m)
    break
M.close()
M.logout()
