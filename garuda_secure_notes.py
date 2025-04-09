import hashlib
import os
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad, unpad

# Function to derive AES key using PBKDF2
def derive_key(password, salt):
    return PBKDF2(password, salt, dkLen=32, count=100000)

# Encrypt the note
def encrypt_note(note, password):
    salt = os.urandom(4)  # 4-byte salt
    key = derive_key(password.encode(), salt)
    iv = os.urandom(16)  # 16-byte IV for AES-CBC
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypted = cipher.encrypt(pad(note.encode(), AES.block_size))

    with open("secure_note.enc", "wb") as f:
        f.write(salt + iv + encrypted)
    print("[+] Note encrypted and saved to secure_note.enc")

# Decrypt the note
def decrypt_note(password):
    try:
        with open("secure_note.enc", "rb") as f:
            data = f.read()
            salt = data[:4]
            iv = data[4:20]
            encrypted = data[20:]

            key = derive_key(password.encode(), salt)
            cipher = AES.new(key, AES.MODE_CBC, iv)
            decrypted = unpad(cipher.decrypt(encrypted), AES.block_size)

            print("[+] Decrypted Note:\n", decrypted.decode())
    except Exception as e:
        print("[-] Decryption failed. Incorrect password or corrupted file.")
        print(e)

# Main flow
print("1. Encrypt a note")
print("2. Decrypt a note")
choice = input("Choose an option: ")

if choice == "1":
    note = input("Enter the note to encrypt: ")
    password = input("Enter a password: ")
    encrypt_note(note, password)
elif choice == "2":
    password = input("Enter the password to decrypt the note: ")
    decrypt_note(password)
else:
    print("Invalid option.")
