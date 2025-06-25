# Text-Encoder-and-Decoder
 A beginner-friendly Python project that encodes and decodes secret messages by adding random characters and shifting letters. Great for practicing string manipulation and logic!
# 🕵️ Secret Text Encoder & Decoder (Python)

A beginner-friendly Python project that lets you encode and decode secret messages by adding random characters and shifting letters. This is a fun and simple way to practice **string manipulation**, **conditional logic**, and **modular programming** in Python.

---

## 🔧 Features

- 🔐 Encode text by:
- Shifting the first letter of each word to the end
- Adding random 3-letter prefixes and suffixes
- 🔓 Decode text by reversing the process
- 📋 Automatically copies results to clipboard using `pyperclip`
- 🧠 Great for beginners learning how to work with strings, functions, and basic logic

---

## 📦 Requirements

- Python 3.x
- `pyperclip` module (install with pip if not already installed):

    ```bash
    pip install pyperclip

---

## 🚀 How It Works

### 🔐 Encoding

- Takes each word from your input.
- If the word is longer than 3 characters:
- Moves the **first letter** to the **end**
- Then removes the original first letter (essentially shifts the first letter to the end)
- Adds **3 random letters** at the start and end of the word

**Example:**  
`Hello World` → `elloh` and `orldw`  
Random characters added → `AbCellohXyZ`, `RtUorldwKqW`

---

### 🔓 Decoding

- Removes the 3 random letters from the **start and end** of each word
- If the word is longer than 3 characters:
- Takes the **last letter** and moves it to the **front**
- This restores the original word

---

## 🧪 Example

```text
Input:   Hello World  
Encoded: XsYellohpQR ZqAorldWpK  
Decoded: Hello World
