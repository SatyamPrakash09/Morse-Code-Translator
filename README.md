# Morse Code Translator 🔡 ⇄ 🟩

A simple yet powerful Python CLI tool to **convert English text to Morse code** and **decode Morse back to text**. Built for learning, testing, and fun!

---

## 🚀 Features

✅ Text → Morse code  
✅ Morse code → Text  
✅ Supports:
- English letters (A–Z, case-insensitive)
- Digits (0–9)
- Punctuation: `. , ? ! ' / ( ) & : ; = + - _ " $ @`
- Spaces (words separated by 3 spaces)

✅ Error handling for unknown characters  
✅ Fully interactive command-line interface

---

## 🧠 How It Works

### 🔡 Text to Morse Code

- Each letter/number is translated using the Morse dictionary.
- Characters are separated by a **single space**.
- Words are separated by **three spaces**.

### 🔁 Morse Code to Text

- Words split by **three spaces**.
- Letters split by **single spaces**.
- Symbols are matched in a **reversed dictionary**.
- Unknown symbols show as `?`.

---

## 🖥️ Usage

### ▶️ Run the Program

```bash
python morse_translator.py

📋 Menu Example
Choose options:
1. Text to Morse code
2. Morse code to Text
3. Exit()
Enter 1, 2 or 3:
```

📌 Example
➡️ Text Input:
Hello, my name is Satyam! I'm 18 years old.

🔃 Morse Code Output:
.... . .-.. .-.. --- --..--   -- -.--   -. .- -- .   .. ...   ... .- - -.-- .- -- -.-.--   .. .----. --   .---- ---..   -.-- . .- .-. ...   --- .-.. -.. .-.-.-

⬅️ Reverse Input:
.... . .-.. .-.. ---   .-- --- .-. .-.. -..

🧾 Text Output:
HELLO WORLD

🧩 Supported Characters
1.Alphabets: A–Z
2.Digits: 0–9
3.Punctuation:
. , ? ! ' / ( ) & : ; = + - _ " $ @
4.Space: interpreted as 3-space word separator

📦 Requirements
• Python 3.x
• No external libraries

📁 File Structure
📂 Morse-Code-Translator
```
├── morse_translator.py   # Main program file
└── README.md             # Project documentation
```

📚 Learn Morse Code (Cheat Sheet):
| Letter | Morse | Letter | Morse | Number | Morse |
| ------ | ----- | ------ | ----- | ------ | ----- |
| A      | .-    | N      | -.    | 0      | ----- |
| B      | -...  | O      | ---   | 1      | .---- |
| C      | -.-.  | P      | .--.  | 2      | ..--- |
| D      | -..   | Q      | --.-  | 3      | ...-- |
| E      | .     | R      | .-.   | 4      | ....- |
| F      | ..-.  | S      | ...   | 5      | ..... |
| G      | --.   | T      | -     | 6      | -.... |
| H      | ....  | U      | ..-   | 7      | --... |
| I      | ..    | V      | ...-  | 8      | ---.. |
| J      | .---  | W      | .--   | 9      | ----. |
| K      | -.-   | X      | -..-  |        |       |
| L      | .-..  | Y      | -.--  |        |       |
| M      | --    | Z      | --..  |        |       |

👨‍💻 Author
Satyam Prakash
[🔗 GitHub](@SatyamPrakash09): [@SatyamPrakash09](@SatyamPrakash09)


🙌 Support
If you found this helpful or fun, consider giving it a ⭐ on GitHub!

