# O(1) - Constant Time
# Definition: The algorithm takes the same amount of time regardless of input size.
def get_first_item(items):
    """
    Always performs one operation regardless of input size
    """
    return items[0] if items else None

"""
Why O(1)?
This function always accesses just one item — no matter how large the list is.
"""

# O(log n) - Logarithmic Time
# Definition: The algorithm cuts the problem in half each time.
def binary_search(sorted_items, target):
    """
    Divides problem size in half at each step
    """
    left, right = 0, len(sorted_items) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if sorted_items[mid] == target:
            return mid
        elif sorted_items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

x = [1, 3, 6, 9, 11, 15, 25, 58, 68, 79, 88]
num = 58

# binary_search(x, num)

"""
Why O(log n)?
Each loop cuts the search space in half — very efficient for large lists.
"""


# O(n) - Linear Time
# Definition: Time grows directly with input size.
def find_maximum(items):
    """
    Must examine each item exactly once
    """
    if not items:
        return None
    
    max_item = items[0]
    for item in items:
        if item > max_item:
            max_item = item
    return max_item


list2 = [85, 45, 77, 33, 87, 23, 11, 45, 65]

# find_maximum(list2)

"""
Why O(n)?
Every element is checked once — time scales linearly with list size.
"""


# O(n²) - Quadratic Time
# Definition: Every element is compared with every other element.
def bubble_sort(items):
    """
    Compares each item with every other item
    """
    n = len(items)
    for i in range(n):
        for j in range(n - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]  # Swapping the values
    return items

list3 = [4, 2, 8, 1, 6, 3, 9, 5, 7]

# list4 = bubble_sort(list3)

# print(list4)

"""
Why O(n²)? O(n^2)
Two nested loops — time grows rapidly with input size.
"""

# O(n log n) - Linearithmic Time
# Definition: A combination of splitting the input (log n) and processing each part (n).

# def merge_sort(items):
#     """
#     Divides and conquers, combining results linearly
#     """
#     if len(items) <= 1:
#         return items
    
#     mid = len(items) // 2
#     left = merge_sort(items[:mid])
#     right = merge_sort(items[mid:])
    
#     # Merge step
#     result = []
#     i = j = 0
#     while i < len(left) and j < len(right):
#         if left[i] <= right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result


def merge_sort(arr):
    # Base case: a list of 0 or 1 element is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Split the list in half
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # Recursive sort on left half
    right = merge_sort(arr[mid:])  # Recursive sort on right half

    # Step 2: Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0

    # Compare elements from both halves and merge in order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    # Add any remaining elements from either half
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

unsorted = [8, 3, 5, 4, 7, 6, 1, 2]
print("Original:", unsorted)
print("Sorted:", merge_sort(unsorted))

"""
Why O(n log n)?
Each split is log n, and merging takes linear time.
"""

# O(2ⁿ) — Exponential Time
# Definition: Time doubles with each additional input — grows extremely fast.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

"""
Why O(2ⁿ)?
Each call creates two more calls — leads to exponential growth.
"""


# O(n!) — Factorial Time
# Definition: Used in problems that require checking every possible ordering (e.g., permutations).
import itertools

def generate_permutations(items):
    return list(itertools.permutations(items))

"""
Why O(n!)?
All possible orderings are generated — factorial growth.
"""