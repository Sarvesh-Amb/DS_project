# 🟩🟨⬛ DS_project: AVL-Powered Wordle Clone

A terminal-based Python implementation of the classic Wordle game, enhanced with a self-balancing binary search tree (**AVL Tree**) for efficient dictionary management, custom word ingestion, and robust validation.

---

## 🚀 Features

* **Self-Balancing AVL Tree:** Replaces linear searches with an $O(\log n)$ balanced binary search tree to guarantee high-performance dictionary lookups.
* **Dynamic Word Ingestion:** Add custom 5-letter secret words on the fly; they are automatically validated, appended persistently to `words.csv`, and dynamically balanced into the runtime AVL tree.
* **Authentic Feedback Engine:** Features a two-pass color-coded evaluation mechanism delivering precise visual feedback:
  * 🟩 **Green:** Correct letter in the correct position.
  * 🟨 **Yellow:** Correct letter in the wrong position.
  * ⬛ **Gray:** Letter not present in the secret word.
* **Terminal-Friendly & Lightweight:** Designed for clean execution in Unix/Linux and Windows terminal environments using standard file I/O operations.

---

## 🧠 Architectural Overview & AVL Tree Logic

To maintain lightning-fast validation as the vocabulary grows, the project utilizes an **AVL Tree**:

1. **Height Balance & Rotations:** Standard Binary Search Trees can degrade into linear chains ($O(n)$) when words are inserted sequentially. The AVL tree monitors balance factors and automatically performs single and double rotations (`_left_rotate`, `_right_rotate`) to maintain a strict logarithmic height.
2. **Search & Verification:** Lookups (`search`) traverse left or right recursively based on alphabetical comparisons against node values.
3. **Persistent File Handling:** Loads and deduplicates 5-letter alphabetical entries from `words.csv`, initializing a robust default vocabulary if no file is present.

---

## 🛠️ Code Structure & Function Reference

| Component / Function | Description |
| :--- | :--- |
| **`AVLNode`** | Represents an individual node holding the word string, left/right child pointers, and height metadata. |
| **`AVLTree` & Rotations** | Manages root reference, height computation, balance factor checks, and single/double rotations (`_left_rotate`, `_right_rotate`). |
| **`insert` / `_insert_rec`** | Handles recursive word insertion with automatic balance restoration. |
| **`search` / `_search_rec`** | Performs logarithmic lookup queries across the AVL tree. |
| **`load_and_initialize_avl`** | Parses, cleans, and deduplicates 5-letter entries from `words.csv` and populates the AVL structure. |
| **`evaluate_guess`** | Executes the two-pass algorithm to analyze guess accuracy and return exact visual indicators (`🟩`, `🟨`, `⬛`). |
| **`play_game`** | Orchestrates the primary game loop, welcome screen, mode selection, attempt tracking (up to 6 tries), and win/loss resolution. |

---

## 📥 Installation & Running the Project

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Sarvesh-Amb/DS_project.git](https://github.com/Sarvesh-Amb/DS_project.git)
   cd DS_project
