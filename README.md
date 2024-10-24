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

### Example Use Cases

- **Finding an element in a large dataset:** If you have a large list of sorted items (e.g., product IDs or timestamps) and want to quickly find the index of a particular value, binary search is a great choice.
- **Looking up words in a dictionary:** Since dictionaries are typically ordered alphabetically, binary search is an efficient way to look up the index of a word.
- **Searching in databases:** Binary search can be applied to sorted indexes in databases, especially when searching for a record by a key (like an ID or timestamp).
- **Checking for the presence of an item in a sorted array:** Instead of scanning the entire list, binary search can tell you whether the item is present or not in logarithmic time.
- **Game development (collision detection, hitboxes):** When you have multiple sorted objects (like hitboxes or collision objects), binary search helps in efficiently finding which object is affected by a particular action.

### Notes

- Ensure the list is **sorted** before using binary search.
- If the target is found, the index is returned.
- If the target is not found, `-1` is returned.
