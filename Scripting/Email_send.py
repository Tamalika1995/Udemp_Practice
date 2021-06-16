import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path
html=Template(Path('index.html').read_text())
email=EmailMessage()
email['From'] = "Tamalika"
email['To'] = 'itamalikachakraborty95@gmail.com'
email['subject']="You won $100000."
email.set_content(html.substitute({'name':1000}),'html')
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('tamalikac1995@gmail.com','Subho@123tama')
    smtp.send_message(email)
    print("all done")