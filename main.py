import csv
import os
import random

class AVLNode:
    """A node in the AVL Tree (Self-Balancing Binary Search Tree)."""
    def __init__(self, word):
        self.word = word
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """An AVL Tree data structure to manage the game's dictionary with self-balancing."""
    def __init__(self):
        self.root = None

    def _height(self, node):
        if not node:
            return 0
        return node.height

    def _balance_factor(self, node):
        if not node:
            return 0
        return self._height(node.left) - self._height(node.right)

    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        # Perform rotation
        x.right = y
        y.left = T2

        # Update heights
        y.height = max(self._height(y.left), self._height(y.right)) + 1
        x.height = max(self._height(x.left), self._height(x.right)) + 1

        return x

    def _left_rotate(self, x):
        y = x.right
        T2 = y.left

        # Perform rotation
        y.left = x
        x.right = T2

        # Update heights
        x.height = max(self._height(x.left), self._height(x.right)) + 1
        y.height = max(self._height(y.left), self._height(y.right)) + 1

        return y

    def insert(self, word):
        self.root = self._insert_rec(self.root, word)

    def _insert_rec(self, node, word):
        # 1. Perform standard BST insertion
        if not node:
            return AVLNode(word)
        
        if word < node.word:
            node.left = self._insert_rec(node.left, word)
        elif word > node.word:
            node.right = self._insert_rec(node.right, word)
        else:
            return node  # Duplicate words are not inserted

        # 2. Update height of this ancestor node
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        # 3. Get the balance factor to check if it became unbalanced
        balance = self._balance_factor(node)

        # 4. Perform rotations if unbalanced

        # Left Left Case
        if balance > 1 and word < node.left.word:
            return self._right_rotate(node)

        # Right Right Case
        if balance < -1 and word > node.right.word:
            return self._left_rotate(node)

        # Left Right Case
        if balance > 1 and word > node.left.word:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        # Right Left Case
        if balance < -1 and word < node.right.word:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    def search(self, word):
        return self._search_rec(self.root, word)

    def _search_rec(self, node, word):
        if not node:
            return False
        if node.word == word:
            return True
        elif word < node.word:
            return self._search_rec(node.left, word)
        else:
            return self._search_rec(node.right, word)

def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def load_and_initialize_avl(filename="words.csv"):
    """Loads words from CSV into an AVL Tree and returns a list of words."""
    avl_tree = AVLTree()
    words = []
    
    if not os.path.exists(filename):
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
        avl_tree.insert(word)
        
    return avl_tree, words

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
    avl_tree, word_list = load_and_initialize_avl(filename)
    
    clear_screen()
    print("========================================")
    print("         WELCOME TO WORDLE (AVL)        ")
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
                # Check if it exists in the AVL Tree, if not, add it
                if not avl_tree.search(secret_word):
                    add_word_to_csv(filename, secret_word)
                    avl_tree.insert(secret_word)
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
