# Project Report: DS_project

## 1. Executive Summary

**DS_project** is a turn-based Wordle game clone developed in Python. Designed as a practical application of core computer science concepts, the project integrates file I/O operations (via CSV files), custom data structuring, and programmatic game logic to recreate and enhance the classic word-guessing experience.

## 2. Project Overview & Objectives

* **Language:** Python

* **Core Mechanics:** Turn-based word guessing, color-coded feedback validation (correct position, correct letter, incorrect letter), and win/loss state management.

* **Data Management:** Dynamic word-list management utilizing CSV data structures.

* **Architectural Focus:** Implementation of self-balancing binary search trees (AVL Trees) to optimize dictionary management, lookups, and word validation.

## 3. Integration of Self-Balancing AVL Trees

To ensure high performance and algorithmic efficiency, the project incorporates an **AVL Tree (Self-Balancing Binary Search Tree)** for managing the game's dictionary database. Key aspects of this implementation include:

* **Algorithmic Efficiency (**$\mathcal{O}(\log n)$**):** Unlike standard Binary Search Trees which can degrade into linear search times ($O(n)$) if populated sequentially, an AVL tree maintains a strictly bounded height via automated single and double rotations (Left-Left, Right-Right, Left-Right, and Right-Left cases). This guarantees logarithmic time complexity for insertions and lookups.

* **Dictionary Validation & Search Logic:** When a player inputs a guess or defines a custom secret word, the system traverses the AVL tree alphabetically. Matching nodes confirm validity, while structural branching guides the search instantly.

* **Dynamic Expansion:** Newly introduced custom words are verified against the tree, appended persistently to the underlying CSV dataset, and seamlessly integrated into the runtime AVL structure through balancing routines.

## 4. Comprehensive Function Architecture

| **Component / Function** | **Description** | 
| **`AVLNode`** | Represents an individual node in the tree containing the word string, left/right child pointers, and height tracking metadata. | 
| **`AVLTree` & Rotations** | Manages root reference, height computation, balance factor evaluation, and single/double rotations (`_left_rotate`, `_right_rotate`) to maintain tree equilibrium. | 
| **Insertion & Search** | Handles recursive word insertion with automatic balance restoration (`_insert_rec`) and logarithmic lookup queries (`_search_rec`). | 
| **File I/O & Initialization (`load_and_initialize_avl`)** | Parses, cleans, and deduplicates 5-letter alphabetical entries from `words.csv` (initializing defaults if absent) and populates the AVL tree. | 
| **Feedback Evaluation (`evaluate_guess`)** | Executes a two-pass algorithm to analyze guess accuracy, mapping characters to exact-position (Green 🟩), misplaced (Yellow 🟨), and absent (Gray ⬛) visual indicators. | 
| **Game Flow (`play_game`)** | Orchestrates user interaction, mode selection (custom vs. random word), attempt tracking, input validation, and win/loss state resolution. | 

## 5. Future Enhancements & Recommendations

* **Expanded Vocabulary & Difficulty Tiers:** Introduce multi-length word categories (e.g., 4, 5, and 6-letter modes) managed across distinct AVL tree instances.

* **Advanced Performance Analytics:** Track session statistics, player streaks, and search traversal performance metrics persistently.

* **Graphical User Interface:** Transition the terminal interface to a graphical platform using `tkinter` or `PyQt` while preserving core data structure logic.