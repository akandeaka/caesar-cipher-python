from string import ascii_uppercase, ascii_lowercase
import tkinter as tk
from tkinter import messagebox

def caesar_cipher(message, shift, mode="encrypt"):
    """
    Encrypt or decrypt a message using the Caesar Cipher.
    :param message: Input text
    :param shift: Number of positions to shift
    :param mode: 'encrypt' or 'decrypt'
    :return: Processed text
    """
    if not message:
        return "Error: Message cannot be empty."
    
    # Ensure shift is within 0-25
    shift = shift % 26
    if mode == "decrypt":
        shift = -shift  # Reverse shift for decryption
    
    # Define alphabets
    upper_alpha = ascii_uppercase  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
    lower_alpha = ascii_lowercase  # abcdefghijklmnopqrstuvwxyz
    result = ""
    
    # Process each character
    for char in message:
        if char.isupper():
            if char in upper_alpha:
                new_index = (upper_alpha.index(char) + shift) % 26
                result += upper_alpha[new_index]
            else:
                result += char
        elif char.islower():
            if char in lower_alpha:
                new_index = (lower_alpha.index(char) + shift) % 26
                result += lower_alpha[new_index]
            else:
                result += char
        else:
            result += char
    
    return result

class CaesarCipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Caesar Cipher")
        self.root.geometry("500x400")
        
        # Message label and input
        self.label_message = tk.Label(root, text="Enter Message:")
        self.label_message.pack(pady=10)
        self.entry_message = tk.Entry(root, width=50)
        self.entry_message.pack(pady=5)
        
        # Shift value label and input
        self.label_shift = tk.Label(root, text="Enter Shift Value (1-25):")
        self.label_shift.pack(pady=10)
        self.entry_shift = tk.Entry(root, width=10)
        self.entry_shift.pack(pady=5)
        
        # Buttons for encrypt and decrypt
        self.button_encrypt = tk.Button(root, text="Encrypt", command=self.encrypt)
        self.button_encrypt.pack(pady=10)
        self.button_decrypt = tk.Button(root, text="Decrypt", command=self.decrypt)
        self.button_decrypt.pack(pady=5)
        
        # Output display
        self.label_result = tk.Label(root, text="Result:")
        self.label_result.pack(pady=10)
        self.text_result = tk.Text(root, height=5, width=50)
        self.text_result.pack(pady=5)
    
    def encrypt(self):
        try:
            message = self.entry_message.get()
            shift_input = self.entry_shift.get()
            
            if not message.strip():
                messagebox.showerror("Error", "Message cannot be empty.")
                return
            if not shift_input.isdigit():
                messagebox.showerror("Error", "Shift value must be a number.")
                return
            
            shift = int(shift_input)
            if shift < 1 or shift > 25:
                messagebox.showerror("Error", "Shift value must be between 1 and 25.")
                return
            
            result = caesar_cipher(message, shift, mode="encrypt")
            self.text_result.delete(1.0, tk.END)
            self.text_result.insert(tk.END, f"Encrypted: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    
    def decrypt(self):
        try:
            message = self.entry_message.get()
            shift_input = self.entry_shift.get()
            
            if not message.strip():
                messagebox.showerror("Error", "Message cannot be empty.")
                return
            if not shift_input.isdigit():
                messagebox.showerror("Error", "Shift value must be a number.")
                return
            
            shift = int(shift_input)
            if shift < 1 or shift > 25:
                messagebox.showerror("Error", "Shift value must be between 1 and 25.")
                return
            
            result = caesar_cipher(message, shift, mode="decrypt")
            self.text_result.delete(1.0, tk.END)
            self.text_result.insert(tk.END, f"Decrypted: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CaesarCipherApp(root)
    root.mainloop()