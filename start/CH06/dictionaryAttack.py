#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By 

#import modules
#import modules
import crypt
import os 

#function to test the password
def test_password(algorithm_salt, hashed_password, password_guess):
    #use salt to hash guess
    hashed_guess= crypt.crypt(password_guess, algorithm_salt)
    #compare salted guess aginst hashed password
    if hashed_guess == hashed_password:
        return True
    return False

#load dictionary file
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/top1000.txt", "r")
password = f.readlines()
f.close()

#Prompt user for the Algorithm and Salt
algorithm_salt = input("What is the algorithm and salt? ")
#Prpmpt user for salted hash
hashed_password = input("what is the full hashed password? ")

#loop through each password
for password in password:
    password = password.strip()
    result = test_password(algorithm_salt, hashed_password, password)
    if result:
        print("Match found: {0}".format(password))
        break




