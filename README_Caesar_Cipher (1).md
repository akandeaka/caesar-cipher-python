
# 🛡️ Caesar Cipher: Text Encryption & Decryption in Python

This project demonstrates how to **encrypt and decrypt messages using the Caesar Cipher** — one of the oldest and simplest methods of encryption. Built using **Python** and a **Tkinter-based GUI**, this tool allows users to enter text, specify a shift value, and see the encrypted or decrypted output instantly.

---

## 🔍 What is the Caesar Cipher?

The **Caesar Cipher** is a substitution encryption technique where each letter in the plaintext is shifted by a fixed number of positions in the alphabet.

- **Invented by**: Julius Caesar, for military communication.
- **Example**: A shift of `3` converts `A → D`, `B → E`, `Z → C` (wraps around).
- **Modern Variant**: ROT13 (rotation by 13 places).

> ⚠️ *Note: Caesar Cipher is not secure for modern use but excellent for learning basic encryption concepts.*

---

## 🔐 How It Works

The encryption uses the following formula:

```
Encryption: En(x) = (x + n) % 26  
Decryption: Dn(x) = (x - n) % 26
```

Where:
- `x` is the letter’s alphabet index (A=0, B=1, ..., Z=25)
- `n` is the shift key

---

## 💬 Example

**Original Message**: `See You Tomorrow`  
**Shift**: `+5`  
**Encrypted Message**: `XJJ DTZ YTRTWWTB`

**Another Example** (Shift = 9):
- Input: `Go to Valley`
- Output: `Px Cx EJUUNH`

---

## 🧰 Tech Stack

- **Language**: Python
- **GUI**: Tkinter (Python’s built-in GUI library)
- **Optional**: Pillow (for GUI enhancements)

---

## 🚀 Features

- ✅ Encrypt and decrypt text using a shift value
- ✅ Case-insensitive text handling
- ✅ User-friendly GUI with `tkinter`
- ✅ Error handling (e.g., invalid input, shift out of range)
- ✅ Modular, reusable cipher function

---

## 🧪 Installation & Setup

### 1. Install Python

- Download from [python.org](https://www.python.org/downloads/)
- Run the installer and **check** `Add Python to PATH`
- Choose "Install Now"

### 2. Verify Environment

Open PowerShell or Terminal:

```bash
python -c "import tkinter; print(tkinter.TkVersion)"
python -c "import PIL; print(PIL.__version__)"  # Optional
```

### 3. Create Project Folder

```bash
mkdir CipherProject
cd CipherProject
```

---

## 📝 Running the Program

1. Save the script as `caesar_cipher_gui.py`
2. Open terminal and run:

```bash
cd CipherProject
python caesar_cipher_gui.py
```

3. GUI Window Includes:
- Input field for the message
- Input for the shift value
- “Encrypt” and “Decrypt” buttons
- Output area showing result

---

## 🧠 Learning Points

### 🔐 Caesar Cipher
- Understand shift encryption with modulo 26
- Recognize limitations of classical ciphers

### 🖼️ GUI Development
- Learn basic Tkinter components: `Entry`, `Button`, `Text`, `messagebox`

### 🛠️ Python Skills
- File/path handling
- Error handling & input validation
- Modular and reusable code structure

---

## 🤝 Contribute

Want to enhance this tool or add new ciphers (like Vigenère or AES)?
- Fork the repo
- Create a branch
- Submit a pull request with your changes

---

## 📂 Folder Structure

```
CipherProject/
├── caesar_cipher_gui.py
└── README.md
```

---

## 📚 Credits

Created by **Akande Akinpelu**  
Prodigy infoTech Cybersecurity Program | Passionate about cryptography and secure systems.

---

## 🧠 Fun Fact

> Did you know?  
The Caesar Cipher, while easily broken today, laid the foundation for all modern encryption!
