import os
from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

print("New key will be generated if there is no existing key.\n")

def keygen():
    gen = input("Would you like to use an existing key (E) or generate a new key (N)? (E/N) ")
    if gen == "N" or gen == "n":
        write_key()
    elif gen == "E" or gen == "e":
        if not os.path.isfile("key.key"): # Check if key.key file exists and run write_key() if it doesn't exist
            write_key() 

def load_key():
    with open('key.key', 'rb') as key_file:
        key = key_file.read()
    return key

keygen()
master_pwd = input("Enter Master Password: ")

key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    if not os.path.isfile('password.txt'):
        print("Password file doesn't exist. Add passwords first.")
        return

    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passwd = data.split("|")
            print("Username:", user, "| Password:", fer.decrypt(passwd.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    
    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view existing ones or quit? (view, add, q) ")
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue