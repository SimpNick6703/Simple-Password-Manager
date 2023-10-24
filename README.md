# Simple-Password-Manager
Simple CLI based Password Manager that uses Fernet from Cryptography Python Library. The program stores a key and user given Username and Password in encrypted format in your current working directory in `key.key` and `password.txt` files respectively. User is given an option to make a new key or use the existing one and make one if none exists.

# Known Bugs
- Using a different Master Password still lists all the credentials in `password.txt`.

# Future Plans
- Explore more possible bugs and fix them.
- Design a GUI and make it more user friendly.
- Clean the code to make it more easy to understand and integrate.
