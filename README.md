# Binary Search Implementation

This repository contains a simple implementation of a **binary search algorithm** in Python.

### Binary Search Overview

Binary search is an efficient algorithm for finding an item from a sorted list of items. It works by repeatedly dividing in half the portion of the list that could contain the item, until you've narrowed the possible locations to just one.

- **Time Complexity:** O(log n)
- **Requirement:** The list must be sorted before running the search.

### How It Works

1. The algorithm checks the middle element of the list.
2. If the middle element is the target, it returns the index.
3. If the middle element is less than the target, it narrows the search to the right half of the list.
4. If the middle element is greater than the target, it narrows the search to the left half of the list.
5. It repeats this process until the target is found or the search space is empty.

### Example Usage

- Ensure the list is **sorted** before using binary search.
- If the target is found, the index is returned.
- If the target is not found, `-1` is returned.
