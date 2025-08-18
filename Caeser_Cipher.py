import pyperclip
import base64
from tkinter import Tk, simpledialog, messagebox, filedialog

# GUI root for dialogs
root = Tk()
root.withdraw()

# === Caesar Cipher ===
def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# === Vigenère Cipher ===
def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            result += caesar_encrypt(char, shift)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = -(ord(key[key_index % len(key)]) - ord('a'))
            result += caesar_encrypt(char, shift)
            key_index += 1
        else:
            result += char
    return result

# === Base64 Encoding/Decoding ===
def base64_encode(text):
    return base64.b64encode(text.encode()).decode()

def base64_decode(text):
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception:
        return "❌ Invalid Base64 input."

# === Utility Functions ===
def copy_to_clipboard(result):
    pyperclip.copy(result)
    messagebox.showinfo("Clipboard", "✅ Result copied to clipboard!")

def save_to_file(result):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    if file_path:
        with open(file_path, "w", encoding='utf-8') as f:
            f.write(result)
        messagebox.showinfo("File Saved", f"✅ Result saved to {file_path}")

# === Main Menu ===
def main():
    while True:
        choice = simpledialog.askstring("Cipher Menu", """
                                        
Cipher Project Menu:

1️ Caesar Cipher
2️ Vigenère Cipher
3️ Base64 Encode/Decode
4️ Exit

Enter option (1/2/3/4):
""")
        if choice == '1':
            handle_caesar()
        elif choice == '2':
            handle_vigenere()
        elif choice == '3':
            handle_base64()
        elif choice == '4' or choice is None:
            break
        else:
            messagebox.showerror("Error", "Please enter 1, 2, 3, or 4.")

# === Caesar Handler ===
def handle_caesar():
    mode = simpledialog.askstring("Caesar Cipher", "Encrypt or Decrypt?").lower()
    text = simpledialog.askstring("Input Text", "Enter text:")
    shift = simpledialog.askinteger("Shift", "Enter shift value (e.g., 3):")

    if text and shift is not None:
        if mode == 'encrypt':
            result = caesar_encrypt(text, shift)
        elif mode == 'decrypt':
            result = caesar_decrypt(text, shift)
        else:
            messagebox.showerror("Error", "Invalid mode.")
            return

        messagebox.showinfo("Result", result)
        copy_to_clipboard(result)
        save_to_file(result)

# === Vigenère Handler ===
def handle_vigenere():
    mode = simpledialog.askstring("Vigenère Cipher", "Encrypt or Decrypt?").lower()
    text = simpledialog.askstring("Input Text", "Enter text:")
    key = simpledialog.askstring("Key", "Enter key (e.g., SECRET):")

    if text and key:
        if mode == 'encrypt':
            result = vigenere_encrypt(text, key)
        elif mode == 'decrypt':
            result = vigenere_decrypt(text, key)
        else:
            messagebox.showerror("Error", "Invalid mode.")
            return

        messagebox.showinfo("Result", result)
        copy_to_clipboard(result)
        save_to_file(result)

# === Base64 Handler ===
def handle_base64():
    mode = simpledialog.askstring("Base64", "Encode or Decode?").lower()
    text = simpledialog.askstring("Input Text", "Enter text:")

    if text:
        if mode == 'encode':
            result = base64_encode(text)
        elif mode == 'decode':
            result = base64_decode(text)
        else:
            messagebox.showerror("Error", "Invalid mode.")
            return

        messagebox.showinfo("Result", result)
        copy_to_clipboard(result)
        save_to_file(result)

# === Run the program ===
if __name__ == '__main__':
    main()