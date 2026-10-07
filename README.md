# 🟩 Wordle DS Clone 🟨

A terminal-based, interactive Wordle game written in Python. This project highlights core Data Structures and Algorithms by implementing a Trie (Prefix Tree) for efficient word management, alongside dynamic CSV file loading and auto-updating.

---

## 🚀 Features

* Interactive Turn-Based Gameplay: Play standard 6-attempt Wordle right in your terminal.
* Custom Word Mode: Choose to play a random word or input your own custom secret word.
* Dynamic CSV Dictionary & Auto-Save: If you enter a custom 5-letter word that isn't in the dictionary, the program automatically sanitizes it, validates it, and appends it to words.csv.
* Tree Data Structure: Uses a Prefix Tree to store, manage, and validate the game's vocabulary.
* Visual Feedback: Uses standard Wordle emoji indicators (🟩 Correct Position, 🟨 Wrong Position, ⬛ Not in Word).

---

## 📂 Project Structure

DS_project/
├── main.py          # Main game loop, Game Master logic, and Trie data structure
├── words.csv        # Dictionary file containing 5-letter words
└── README.md        # Project documentation

---

## 🛠️ Getting Started & Installation

### Prerequisites
Make sure you have Python 3 installed on your system.

### 1. Clone the Repository
Open your terminal and clone the project:
git clone https://github.com/Sarvesh-Amb/DS_project.git
cd DS_project

### 2. Run the Game
Execute the main script to start playing:
python3 main.py

---

## 🎮 How to Play

1. Run the script. Choose whether you want the game to pick a random word or if you want to make your own secret word.
2. If you choose a random word, you can optionally choose to peek at it or keep it a surprise.
3. If you make your own word, type a valid 5-letter alphabetic word (spaces and case will be automatically handled/sanitized).
4. Enter your guesses and use the feedback signs to narrow down the answer:
   * 🟩 Green: Correct letter in the correct position.
   * 🟨 Yellow: Correct letter in the wrong position.
   * ⬛ Gray: Letter is not in the word.
5. Guess the word within 6 attempts to win!

---

## 💡 Data Structure Highlight: Trie
The game uses a Trie (Prefix Tree) data structure to store words. Instead of linear searching through a list every time a word needs validation, the Trie allows for fast lookups, making vocabulary checks highly efficient.
