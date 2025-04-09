# 🛡️ Garuda Secure Notes

A Python-based secure note encryption and decryption system using AES-CBC with salted password-based key derivation.  
This project is part of the **Garuda Sentinel** cybersecurity mission to practice strong cryptographic implementations.

---

## 🔐 Features

- AES-CBC encryption for secure file storage
- Password-based key derivation using PBKDF2 with random salt
- Salt and IV stored along with the encrypted file
- Decryption only possible with correct password
- Lightweight and file-based; no external database

---

## 🧪 How It Works

1. User inputs a strong password.
2. A 4-byte random salt is generated.
3. A 32-byte key is derived from password + salt using PBKDF2.
4. A 16-byte IV is generated for AES-CBC mode.
5. User's note is encrypted and saved with `[salt][IV][ciphertext]` structure.
6. For decryption, password is used to regenerate the key using extracted salt and IV.
7. If password matches, note is decrypted and shown; else, it fails securely.

---

## 📚 What You Learn

- AES encryption (CBC mode)
- Salted password hashing using PBKDF2
- File handling with binary I/O
- Secure handling of encryption keys and IVs
- Real-world secure note simulation

---

---

## 🛡️ Part of Garuda Sentinel Mission

> "Inspired by **Garuda**, the divine protector – this project guards digital gates and strengthens cybersecurity awareness."

---

## ✅ Status

🔒 Secure | 💡 Educational | 🎯 Portfolio-Ready

---

## 📌 Next Up

- GUI Interface using Tkinter or PyQt
- Auto-delete decrypted file after read
- Add timestamp-based file expiry
- Optional biometric backup

---

## 📎 Author

**Srinath Reddy**  
Garuda Sentinel | Cybersecurity Student & Enthusiast  
GitHub: [@Srinathreddy36](https://github.com/Srinathreddy36)

---

## 🧠 Inspired By

Book: *Serious Cryptography* by Jean-Philippe Aumasson  
Mission: Build practical security tools for real-world use cases

