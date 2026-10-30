from Crypto.Cipher import AES
from Crypto import Random
import hashlib
import random

BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s: s[:-ord(s[len(s) - 1:])]

plain_text = "fsociety."
key = hashlib.sha256(b"357").digest() 
print("Key:", key)

plain_text = pad(plain_text)
iv = Random.new().read(BS)
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher_text = iv + cipher.encrypt(plain_text.encode())
print("\nCiphered text:", cipher_text)

correctPassword = "357"
wrongPasswords = []
password = ""
length = 3
chars = "1234567890"
run = True

while run:
    password = ""
    for i in range(length):
        password += random.choice(chars)
    if password not in wrongPasswords:
        if password != correctPassword:
            print(password)
            wrongPasswords.append(password)
        else:
            run = False
            print(f"{password} is correct")
            break
iv = cipher_text[:BS]
cipher = AES.new(key, AES.MODE_CBC, iv)
plain_text = unpad(cipher.decrypt(cipher_text[BS:])).decode()
print("\nPlain text:", plain_text)
