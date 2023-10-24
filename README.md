# Simple-Password-Manager
Simple CLI based Password Manager that uses Fernet from Cryptography Python Library. The program stores a key and user given Username and Password in encrypted format in your current working directory in `key.key` and `password.txt` files respectively. User is given an option to make a new key or use the existing one and make one if none exists.

# How to use
1. Install `cryptography` python library using `pip` using any command line interface like Terminal or Powershell:
   - Command to install `cryptography`: `pip install cryptography`
     If the above doesn't work then try:
      - `python -m pip install cryptography`
      - `python3 -m pip3 install cryptography`
2. Run the code when in the code's directory:
   - Command to run the code: `python passmanager.py`
     If the above doesn't work then try again with `python3 passmanager.py`.
     
## Known Bugs
- Using a different Master Password still lists all the credentials in `password.txt`.

# Future Plans
- Explore more possible bugs and fix them.
- Design a GUI and make it more user friendly.
- Clean the code to make it more easy to understand and integrate.
