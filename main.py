import csv
import os
import random

class TrieNode:
    """A node in the Trie (Prefix Tree) data structure for word storage and lookup."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordTrie:
    """A Trie data structure to manage the game's dictionary."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_and_initialize_trie(filename="words.csv"):
    """Loads words from CSV into a Trie and returns a list of words."""
    trie = WordTrie()
    words = []
    
    if not os.path.exists(filename):
        # Create default file if it doesn't exist
        default_words = ["apple", "beach", "chair", "drive", "eagle", "flame", "grape", "house"]
        with open(filename, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            for w in default_words:
                writer.writerow([w])
        words = default_words
    else:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                for item in row:
                    cleaned = item.strip().lower()
                    if len(cleaned) == 5 and cleaned.isalpha():
                        words.append(cleaned)
        words = list(set(words))

    for word in words:
        trie.insert(word)
        
    return trie, words

def add_word_to_csv(filename, word):
    """Appends a new word to the CSV file."""
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([word])

def evaluate_guess(guess, secret_word):
    """
    Evaluates the user's guess against the secret word.
    Returns visual feedback signs: 🟩 (Green), 🟨 (Yellow), ⬛ (Gray)
    """
    guess = guess.lower()
    secret_chars = list(secret_word)
    feedback = ['⬛'] * 5
    
    # First pass: Check for greens (correct position)
    for i in range(5):
        if guess[i] == secret_chars[i]:
            feedback[i] = '🟩'
            secret_chars[i] = None

    # Second pass: Check for yellows (wrong position)
    for i in range(5):
        if feedback[i] == '🟩':
            continue
        if guess[i] in secret_chars:
            feedback[i] = '🟨'
            secret_chars[secret_chars.index(guess[i])] = None
            
    return "".join(feedback)

def play_game():
    filename = "words.csv"
    trie, word_list = load_and_initialize_trie(filename)
    
    clear_screen()
    print("========================================")
    print("         WELCOME TO WORDLE          ")
    print("========================================")
    print("1. Make your own secret word")
    print("2. Choose a random secret word")
    
    choice = input("\nEnter your choice (1 or 2): ").strip()
    
    secret_word = ""
    
    if choice == '1':
        while True:
            custom_word = input("\nEnter your 5-letter secret word: ").strip().lower()
            if len(custom_word) == 5 and custom_word.isalpha():
                secret_word = custom_word
                # Check if it exists in the Trie/CSV, if not, add it
                if not trie.search(secret_word):
                    add_word_to_csv(filename, secret_word)
                    trie.insert(secret_word)
                    print(f"[+] '{secret_word}' was added to the dictionary!")
                break
            else:
                print("[-] Invalid input! Must be strictly 5 alphabetic letters with no spaces.")
    else:
        secret_word = random.choice(word_list)
        see_word = input("\nDo you want to see the secret word before starting? (y/n): ").strip().lower()
        if see_word == 'y':
            print(f"[DEBUG] The secret word is: **{secret_word}**")
            input("Press Enter to start playing...")

    # Clear screen before starting the game turns
    clear_screen()
    
    max_attempts = 6
    print(f"Game started! You have {max_attempts} attempts to guess the 5-letter word.\n")
    
    for attempt in range(1, max_attempts + 1):
        while True:
            guess = input(f"Attempt {attempt}/{max_attempts} - Enter your guess: ").strip().lower()
            if len(guess) == 5 and guess.isalpha():
                break
            print("[-] Invalid guess. Please enter a 5-letter alphabetic word.")
            
        feedback = evaluate_guess(guess, secret_word)
        print(f"Guess: {guess.upper()}  -->  Feedback: {feedback}\n")
        
        if guess == secret_word:
            print(f"🎉 Congratulations! You guessed the word '{secret_word.upper()}' correctly in {attempt} attempts!")
            return

    print(f"❌ Game Over! You ran out of attempts. The secret word was: **{secret_word.upper()}**")

if __name__ == "__main__":
    play_game()