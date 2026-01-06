"""
================================================================================
                            RECURSION THEORY IN PYTHON
================================================================================
Recursion: A technique where a function calls itself to solve smaller 
           subproblems until it reaches a base case.

Key Components of Recursion:
1. Base Case    - The stopping condition (prevents infinite recursion)
2. Recursive Case - The function calls itself with a smaller/simpler input

Types of Recursion:
- Tail Recursion      : Recursive call is the LAST operation
- Non-Tail Recursion  : Operations happen AFTER the recursive call
- Tree Recursion      : Function makes multiple recursive calls (e.g., Fibonacci)
- Indirect Recursion  : Function A calls B, which calls A
- Nested Recursion    : Recursive call is passed as argument to itself
================================================================================
"""

# ==============================================================================
# 1. BASIC RECURSION - Infinite Recursion Example (DO NOT UNCOMMENT)
# ==============================================================================
# This demonstrates what happens without a base case - INFINITE LOOP!
# def greet():
#     print("greet")
#     greet()  # No base case = infinite recursion = stack overflow!
# greet()


# ==============================================================================
# 2. RECURSION WITH BASE CASE - Print count from 0 to 3
# ==============================================================================
# Time Complexity: O(n) | Space Complexity: O(n) - recursion stack
# def func(count):
#     if count == 4:       # Base case: stop when count reaches 4
#         return
#     print(count)         # Process current value
#     count += 1           # Modify parameter
#     func(count)          # Recursive call with updated value
# func(0)  # Output: 0, 1, 2, 3


# ==============================================================================
# 3. TAIL RECURSION - Print name N times
# ==============================================================================
# Tail Recursion: The recursive call is the LAST operation in the function
# More memory efficient in languages with tail call optimization
# Time Complexity: O(n) | Space Complexity: O(n)
# def print_name(name, n):
#     if n == 0:           # Base case: stop when n reaches 0
#         return
#     print(name)          # Process first
#     print_name(name, n-1)  # Recursive call is the LAST operation (tail)
# print_name("geet", 5)  # Output: prints "geet" 5 times


# ==============================================================================
# 4. RECURSION USING PARAMETERS - Print X, N times
# ==============================================================================
# Similar to tail recursion - passing parameters to control recursion
# Time Complexity: O(n) | Space Complexity: O(n)
# def print_x_n_times(x, n):
#     if n == 0:           # Base case
#         return
#     print(x)             # Print value
#     print_x_n_times(x, n-1)  # Decrement n and recurse
# print_x_n_times("hello", 3)  # Output: prints "hello" 3 times


# ==============================================================================
# 5. NON-TAIL RECURSION (FUNCTIONAL RECURSION) - Factorial
# ==============================================================================
# Non-Tail: Operations happen AFTER the recursive call returns
# Formula: n! = n * (n-1)! where 0! = 1
# Example: 5! = 5 * 4 * 3 * 2 * 1 = 120
# Time Complexity: O(n) | Space Complexity: O(n)
# def factorial(n):
#     if n == 0:           # Base case: 0! = 1
#         return 1
#     return n * factorial(n-1)  # Multiplication happens AFTER recursive call
# print(factorial(5))  # Output: 120


# ==============================================================================
# 6. PARAMETRIZED RECURSION - Sum of 1 to N
# ==============================================================================
# Two approaches: Parametrized (carry sum) vs Functional (return sum)
# Formula: sum(n) = n + (n-1) + (n-2) + ... + 1
# Example: sum(5) = 5 + 4 + 3 + 2 + 1 = 15
# Time Complexity: O(n) | Space Complexity: O(n)

# Approach 1: Functional Recursion (return values)
# def sum_1_to_n(n):
#     if n == 0:           # Base case: sum of 0 is 0
#         return 0
#     return n + sum_1_to_n(n-1)  # Add n to sum of (n-1)
# print(sum_1_to_n(5))   # Output: 15
# print(sum_1_to_n(10))  # Output: 55

# Approach 2: Parametrized Recursion (carry accumulator)
# def sum_param(total, i, n):
#     if i > n:            # Base case: when i exceeds n
#         return total
#     total += i           # Add current value to accumulator
#     return sum_param(total, i+1, n)  # Move to next number
# print(sum_param(0, 1, 5))  # Output: 15


# ==============================================================================
# 7. FACTORIAL - Complete Implementation
# ==============================================================================
# Formula: n! = n * (n-1) * (n-2) * ... * 1, where 0! = 1! = 1
# Time Complexity: O(n) | Space Complexity: O(n)
# def factorial(n):
#     if n == 0 or n == 1:  # Base case: 0! = 1! = 1
#         return 1
#     return n * factorial(n-1)  # n! = n * (n-1)!
# print(factorial(5))  # Output: 120 (5*4*3*2*1)
# print(factorial(0))  # Output: 1


# ==============================================================================
# 8. ARRAY REVERSAL USING RECURSION - Two Pointer Approach
# ==============================================================================
# Swap elements from both ends and move towards center
# Time Complexity: O(n/2) = O(n) | Space Complexity: O(n/2) = O(n)
# def reverse_array(arr, start, end):
#     if start >= end:     # Base case: pointers meet or cross
#         return
#     arr[start], arr[end] = arr[end], arr[start]  # Swap elements
#     reverse_array(arr, start + 1, end - 1)       # Move pointers inward
# array = [1, 2, 3, 4, 5]
# reverse_array(array, 0, len(array) - 1)
# print(array)  # Output: [5, 4, 3, 2, 1]


# ==============================================================================
# 9. PALINDROME CHECK USING RECURSION - Two Pointer Approach
# ==============================================================================
# Compare characters from both ends moving towards center
# Time Complexity: O(n/2) = O(n) | Space Complexity: O(n/2) = O(n)
# def is_palindrome(s, start, end):
#     if start >= end:     # Base case: all characters matched
#         return True
#     if s[start] != s[end]:  # Characters don't match
#         return False
#     return is_palindrome(s, start + 1, end - 1)  # Check inner substring
# string = "racecar"
# result = is_palindrome(string, 0, len(string) - 1)
# print(f"'{string}' is palindrome: {result}")  # Output: True


# ==============================================================================
# 10. FIBONACCI SERIES - Tree Recursion
# ==============================================================================
# Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# Formula: fib(n) = fib(n-1) + fib(n-2)
# Base Cases: fib(0) = 0, fib(1) = 1
#
# This is TREE RECURSION because each call branches into TWO recursive calls
#
#                    fib(5)
#                   /      \
#              fib(4)      fib(3)
#             /    \       /    \
#         fib(3)  fib(2) fib(2) fib(1)
#         /   \    ...    ...
#     fib(2) fib(1)
#
# Time Complexity: O(2^n) - Exponential (many repeated calculations)
# Space Complexity: O(n) - Maximum depth of recursion stack
# ==============================================================================

def fib(num):
    """
    Calculate the nth Fibonacci number using recursion.
    
    Args:
        num: The index in Fibonacci sequence (0-indexed)
    
    Returns:
        The Fibonacci number at position 'num'
    
    Examples:
        fib(0) = 0, fib(1) = 1, fib(5) = 5, fib(10) = 55
    """
    # Base case: fib(0) = 0, fib(1) = 1
    if num == 0 or num == 1:
        return num
    
    # Recursive case: fib(n) = fib(n-1) + fib(n-2)
    # This creates a tree of recursive calls (Tree Recursion)
    return fib(num - 1) + fib(num - 2)


# ==============================================================================
# TEST CASES
# ==============================================================================
print("=" * 50)
print("FIBONACCI SERIES - Test Results")
print("=" * 50)
print(f"fib(0)  = {fib(0)}")   # Output: 0  (base case)
print(f"fib(1)  = {fib(1)}")   # Output: 1  (base case)
print(f"fib(5)  = {fib(5)}")   # Output: 5  (sequence: 0,1,1,2,3,5)
print(f"fib(6)  = {fib(6)}")   # Output: 8  (sequence: 0,1,1,2,3,5,8)
print(f"fib(10) = {fib(10)}")  # Output: 55
print("=" * 50)

