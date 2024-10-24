from typing import List

"""
Runs a vanilla binarysearch
This requires the list to be sorted already.
We check the middle element to see if it is the target everytime.
If it isn't the target:
we check if its less than the target or greater than the target
if less than it will set left to the middle + 1
if greater than it will set right to the middle - 1
Time Complexity: O(Log(n))
"""
def binary_search(arr: List[int], target: int) -> int:
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right)

        if arr[mid] is target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


"""
Sample
"""

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Binary Search in list for 8")
print(binary_search(list, 8))
print("Binary Search in list for 3")
print(binary_search(list, 3))
print("Binary Search in list for 5")
print(binary_search(list, 5))
print("Binary Search in list for 100")
print(binary_search(list, 100))
