"""
================================================================================
                    PYTHON FUNDAMENTALS & DSA PRACTICE
================================================================================
This file contains fundamental programming concepts and Data Structures & 
Algorithms (DSA) practice problems with detailed explanations.

Topics Covered:
1. Counting Digits in a Number
2. Palindrome (Number & String)
3. Armstrong Number
4. Factorial (Iterative & Recursive)
5. Frequency Map / Hashing
6. Character Hashing

Author: Practice File
Date: December 2024
================================================================================
"""

import math

# ==============================================================================
# SECTION 1: COUNTING DIGITS IN A NUMBER
# ==============================================================================
"""
THEORY:
-------
Counting digits means finding how many digits are present in a given number.
For example: 112323 has 6 digits.

APPROACHES:
1. Iterative Approach (Loop) - Repeatedly divide by 10 until number becomes 0
2. Mathematical Approach (Logarithm) - Use log10 to calculate digits directly

TIME COMPLEXITY:
- Iterative: O(d) where d = number of digits
- Mathematical: O(1) - constant time
"""

def count_digits_iterative(n):
    """
    Count digits using iterative approach (while loop).
    
    Logic: 
    - Divide number by 10 repeatedly
    - Each division removes one digit
    - Count how many times we can divide before reaching 0
    
    Args:
        n (int): The number to count digits of
    
    Returns:
        int: Number of digits in n
    
    Example:
        >>> count_digits_iterative(112323)
        6
    """
    if n == 0:
        return 1  # Special case: 0 has 1 digit
    
    num = abs(n)  # Handle negative numbers
    count = 0
    
    while num > 0:
        num = num // 10  # Integer division removes last digit
        count += 1
    
    return count


def count_digits_mathematical(n):
    """
    Count digits using mathematical approach (logarithm).
    
    Logic:
    - log10(n) gives the power of 10 needed to represent n
    - floor(log10(n)) + 1 gives the number of digits
    - Example: log10(100) = 2, so 100 has 2+1 = 3 digits
    
    Args:
        n (int): The number to count digits of
    
    Returns:
        int: Number of digits in n
    
    Example:
        >>> count_digits_mathematical(112323)
        6
    """
    if n == 0:
        return 1  # Special case: 0 has 1 digit
    
    return math.floor(math.log10(abs(n))) + 1


# Example Usage - Counting Digits
print("=" * 60)
print("SECTION 1: COUNTING DIGITS")
print("=" * 60)
n = 112323
print(f"Number: {n}")
print(f"Digits (Iterative Method): {count_digits_iterative(n)}")
print(f"Digits (Mathematical Method): {count_digits_mathematical(n)}")
print()


# ==============================================================================
# SECTION 2: PALINDROME CHECK (NUMBER & STRING)
# ==============================================================================
"""
THEORY:
-------
A PALINDROME is a sequence that reads the same forward and backward.

Examples:
- Number Palindromes: 121, 12321, 1001
- String Palindromes: "racecar", "madam", "level"

APPROACHES:
1. String Reversal - Convert to string and compare with reversed version
2. Two Pointer - Compare characters from both ends moving towards center
3. Mathematical (for numbers) - Reverse the number mathematically

TIME COMPLEXITY: O(n) where n = length of string/number of digits
SPACE COMPLEXITY: O(n) for string method, O(1) for two-pointer
"""

def is_palindrome_number(n):
    """
    Check if a number is a palindrome using string reversal.
    
    Logic:
    - Convert number to string
    - Reverse the string using slicing [::-1]
    - Compare original with reversed
    
    Args:
        n (int): Number to check
    
    Returns:
        bool: True if palindrome, False otherwise
    
    Example:
        >>> is_palindrome_number(121)
        True
        >>> is_palindrome_number(123)
        False
    """
    original = str(n)
    reversed_num = original[::-1]  # Python slicing to reverse
    return original == reversed_num


def is_palindrome_string(s):
    """
    Check if a string is a palindrome using string reversal.
    
    Args:
        s (str): String to check
    
    Returns:
        bool: True if palindrome, False otherwise
    
    Example:
        >>> is_palindrome_string("racecar")
        True
        >>> is_palindrome_string("hello")
        False
    """
    original = s.lower()  # Convert to lowercase for case-insensitive comparison
    reversed_str = original[::-1]
    return original == reversed_str


def is_palindrome_two_pointer(s):
    """
    Check if a string is a palindrome using two-pointer technique.
    
    Logic:
    - Use two pointers: one at start, one at end
    - Compare characters at both pointers
    - Move pointers towards center
    - If all characters match, it's a palindrome
    
    Args:
        s (str): String to check
    
    Returns:
        bool: True if palindrome, False otherwise
    
    Time Complexity: O(n)
    Space Complexity: O(1) - no extra space needed
    """
    s = s.lower()
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True


# Example Usage - Palindrome
print("=" * 60)
print("SECTION 2: PALINDROME CHECK")
print("=" * 60)

# Number palindrome examples
numbers = [121, 12321, 123, 1001]
print("Number Palindrome Check:")
for num in numbers:
    result = is_palindrome_number(num)
    print(f"  {num} -> {'Palindrome ✓' if result else 'Not Palindrome ✗'}")

# String palindrome examples
strings = ["racecar", "madam", "hello", "level", "python"]
print("\nString Palindrome Check:")
for string in strings:
    result = is_palindrome_string(string)
    print(f"  '{string}' -> {'Palindrome ✓' if result else 'Not Palindrome ✗'}")
print()


# ==============================================================================
# SECTION 3: ARMSTRONG NUMBER
# ==============================================================================
"""
THEORY:
-------
An ARMSTRONG NUMBER (also called Narcissistic Number) is a number that is 
equal to the sum of its own digits each raised to the power of the number 
of digits.

Formula: For n-digit number, sum of (each digit)^n = original number

Examples:
- 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153 ✓ (3-digit Armstrong)
- 1634 = 1⁴ + 6⁴ + 3⁴ + 4⁴ = 1 + 1296 + 81 + 256 = 1634 ✓ (4-digit Armstrong)
- 371 = 3³ + 7³ + 1³ = 27 + 343 + 1 = 371 ✓ (3-digit Armstrong)
- 9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴ = 6561 + 256 + 2401 + 256 = 9474 ✓

TIME COMPLEXITY: O(d) where d = number of digits
SPACE COMPLEXITY: O(1)
"""

def is_armstrong_number(n):
    """
    Check if a number is an Armstrong number.
    
    Logic:
    1. Count the number of digits (d)
    2. For each digit, raise it to power d
    3. Sum all the powered digits
    4. If sum equals original number, it's Armstrong
    
    Args:
        n (int): Number to check
    
    Returns:
        bool: True if Armstrong number, False otherwise
    
    Example:
        >>> is_armstrong_number(153)
        True
        >>> is_armstrong_number(1634)
        True
        >>> is_armstrong_number(123)
        False
    """
    original = n
    num_digits = len(str(n))  # Count number of digits
    
    sum_of_powers = 0
    temp = n
    
    while temp > 0:
        digit = temp % 10           # Extract last digit
        sum_of_powers += digit ** num_digits  # Raise to power and add
        temp = temp // 10           # Remove last digit
    
    return sum_of_powers == original


def find_armstrong_numbers_in_range(start, end):
    """
    Find all Armstrong numbers in a given range.
    
    Args:
        start (int): Start of range (inclusive)
        end (int): End of range (inclusive)
    
    Returns:
        list: List of Armstrong numbers in the range
    """
    armstrong_list = []
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_list.append(num)
    return armstrong_list


# Example Usage - Armstrong Number
print("=" * 60)
print("SECTION 3: ARMSTRONG NUMBER")
print("=" * 60)

test_numbers = [153, 370, 371, 407, 1634, 8208, 9474, 123, 456]
print("Armstrong Number Check:")
for num in test_numbers:
    result = is_armstrong_number(num)
    if result:
        digits = len(str(num))
        breakdown = " + ".join([f"{d}^{digits}" for d in str(num)])
        print(f"  {num} = {breakdown} = {num} ✓ Armstrong")
    else:
        print(f"  {num} -> Not Armstrong ✗")

print(f"\nArmstrong numbers from 1 to 1000: {find_armstrong_numbers_in_range(1, 1000)}")
print()


# ==============================================================================
# SECTION 4: FACTORIAL
# ==============================================================================
"""
THEORY:
-------
FACTORIAL of a non-negative integer n (denoted as n!) is the product of all 
positive integers less than or equal to n.

Formula: n! = n × (n-1) × (n-2) × ... × 2 × 1

Special Cases:
- 0! = 1 (by definition)
- 1! = 1

Examples:
- 5! = 5 × 4 × 3 × 2 × 1 = 120
- 4! = 4 × 3 × 2 × 1 = 24
- 3! = 3 × 2 × 1 = 6

APPROACHES:
1. Iterative - Use a loop to multiply numbers
2. Recursive - Function calls itself with smaller input

TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: 
- Iterative: O(1)
- Recursive: O(n) due to call stack
"""

def factorial_iterative(n):
    """
    Calculate factorial using iterative approach (loop).
    
    Logic:
    - Start with result = 1
    - Multiply result by each number from 1 to n
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    
    Example:
        >>> factorial_iterative(5)
        120
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    result = 1
    for i in range(1, n + 1):
        result *= i  # result = result * i
    
    return result


def factorial_recursive(n):
    """
    Calculate factorial using recursive approach.
    
    Logic (Recursion):
    - Base Case: if n is 0 or 1, return 1
    - Recursive Case: n! = n × (n-1)!
    
    How it works for n=5:
        factorial(5)
        = 5 * factorial(4)
        = 5 * 4 * factorial(3)
        = 5 * 4 * 3 * factorial(2)
        = 5 * 4 * 3 * 2 * factorial(1)
        = 5 * 4 * 3 * 2 * 1
        = 120
    
    Args:
        n (int): Non-negative integer
    
    Returns:
        int: Factorial of n
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    # Base Case
    if n == 0 or n == 1:
        return 1
    
    # Recursive Case
    return n * factorial_recursive(n - 1)


def print_factorials_up_to(n):
    """
    Print factorials of all numbers from 1 to n.
    
    Args:
        n (int): Upper limit
    """
    print(f"Factorials from 1 to {n}:")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        print(f"  {i}! = {factorial}")


# Example Usage - Factorial
print("=" * 60)
print("SECTION 4: FACTORIAL")
print("=" * 60)

n = 5
print(f"Factorial of {n} (Iterative): {factorial_iterative(n)}")
print(f"Factorial of {n} (Recursive): {factorial_recursive(n)}")
print()
print_factorials_up_to(10)
print()


# ==============================================================================
# SECTION 5: FREQUENCY MAP / HASHING (NUMBERS)
# ==============================================================================
"""
THEORY:
-------
HASHING is a technique of pre-storing values into a data structure (like 
dictionary or list) for faster access. Instead of searching every time, 
we store the count/frequency once and retrieve in O(1) time.

FREQUENCY MAP (Hash Map) stores:
- Key: The element
- Value: Number of times it appears (frequency)

WHY USE HASHING?
- Without Hashing (Brute Force): O(n²) - For each query, scan entire array
- With Hashing: O(n) preprocessing + O(1) per query

APPROACHES:
1. Dictionary with manual check (if-else)
2. Dictionary with .get() method (cleaner)
3. Array-based hashing (when range is known and small)

TIME COMPLEXITY: O(n) for building, O(1) for lookup
SPACE COMPLEXITY: O(n) for storing frequencies
"""

def frequency_map_basic(nums):
    """
    Create frequency map using basic if-else approach.
    
    Logic:
    - Iterate through each element
    - If element exists in dict, increment count
    - If not, add it with count = 1
    
    Args:
        nums (list): List of numbers
    
    Returns:
        dict: Frequency map {element: count}
    
    Example:
        >>> frequency_map_basic([1, 2, 2, 3, 3, 3])
        {1: 1, 2: 2, 3: 3}
    """
    freq_map = {}
    
    for num in nums:
        if num in freq_map:
            freq_map[num] += 1  # Element exists, increment
        else:
            freq_map[num] = 1   # New element, initialize to 1
    
    return freq_map


def frequency_map_optimal(nums):
    """
    Create frequency map using .get() method (Pythonic way).
    
    Logic:
    - dict.get(key, default) returns value if key exists, else default
    - We get current count (or 0 if new) and add 1
    
    Args:
        nums (list): List of numbers
    
    Returns:
        dict: Frequency map {element: count}
    """
    freq_map = {}
    
    for num in nums:
        # get() returns 0 if num not in dict, then we add 1
        freq_map[num] = freq_map.get(num, 0) + 1
    
    return freq_map


def frequency_map_array_based(nums, max_val):
    """
    Create frequency map using array (when range is known).
    
    Logic:
    - Create array of size (max_val + 1) initialized to 0
    - Use element value as index, increment that position
    - Only works when elements are non-negative integers in known range
    
    Advantage: Faster than dictionary for small, known ranges
    
    Args:
        nums (list): List of numbers (0 to max_val)
        max_val (int): Maximum possible value in nums
    
    Returns:
        list: Frequency array where index = element, value = count
    
    Example:
        >>> frequency_map_array_based([1, 2, 2, 3], 3)
        [0, 1, 2, 1]  # index 0=0, index 1=1, index 2=2, index 3=1
    """
    freq_array = [0] * (max_val + 1)  # Initialize array with zeros
    
    for num in nums:
        if 0 <= num <= max_val:
            freq_array[num] += 1  # Use element as index
    
    return freq_array


def count_occurrences_brute_force(nums, queries):
    """
    Count occurrences using brute force (for comparison).
    
    Time Complexity: O(n * q) where n=array size, q=number of queries
    This is INEFFICIENT for large inputs!
    """
    results = {}
    for query in queries:
        count = 0
        for num in nums:
            if num == query:
                count += 1
        results[query] = count
    return results


def count_occurrences_with_hashing(nums, queries):
    """
    Count occurrences using hashing (optimal approach).
    
    Time Complexity: O(n + q) - Much better!
    - O(n) to build frequency map
    - O(1) per query lookup
    """
    # Step 1: Build frequency map (preprocessing)
    freq_map = frequency_map_optimal(nums)
    
    # Step 2: Answer queries in O(1) each
    results = {}
    for query in queries:
        results[query] = freq_map.get(query, 0)
    
    return results


# Example Usage - Frequency Map
print("=" * 60)
print("SECTION 5: FREQUENCY MAP / HASHING (NUMBERS)")
print("=" * 60)

nums = [2, 3, 5, 5, 6, 7, 8, 3, 5, 6, 3, 5, 2, 5, 6, 7, 7, 2, 2, 5, 7, 3, 5, 6, 7, 8, 9, 0, 1, 2, 3, 4, 5]
queries = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(f"Array: {nums[:15]}... (truncated)")
print(f"Queries: {queries}")
print()

# Method 1: Basic approach
freq_basic = frequency_map_basic(nums)
print(f"Frequency Map (Basic): {freq_basic}")

# Method 2: Optimal approach with .get()
freq_optimal = frequency_map_optimal(nums)
print(f"Frequency Map (Optimal): {freq_optimal}")

# Method 3: Array-based (for small known range)
freq_array = frequency_map_array_based(nums, 9)
print(f"Frequency Array (0-9): {freq_array}")
print(f"  Interpretation: 0 appears {freq_array[0]}x, 1 appears {freq_array[1]}x, etc.")

# Query results
print("\nQuery Results (using hashing):")
results = count_occurrences_with_hashing(nums, queries)
for q, count in results.items():
    print(f"  Number {q} appears {count} times")
print()


# ==============================================================================
# SECTION 6: CHARACTER HASHING
# ==============================================================================
"""
THEORY:
-------
CHARACTER HASHING is the same concept as number hashing, but applied to 
characters in a string. We count the frequency of each character.

APPROACHES:
1. Dictionary-based: Works for any characters (Unicode, special chars, etc.)
2. Array-based: Efficient for limited character set (e.g., only lowercase a-z)

ARRAY-BASED CHARACTER HASHING:
- Create array of size 26 (for a-z)
- Convert character to index using: index = ord(char) - ord('a')
- ord('a') = 97, ord('b') = 98, ... ord('z') = 122
- So 'a' -> index 0, 'b' -> index 1, ... 'z' -> index 25

USE CASES:
- Anagram detection
- Character frequency analysis
- String pattern matching
- Compression algorithms

TIME COMPLEXITY: O(n) where n = string length
SPACE COMPLEXITY: O(k) where k = number of unique characters
"""

def char_frequency_basic(s):
    """
    Count character frequency using basic dictionary approach.
    
    Args:
        s (str): Input string
    
    Returns:
        dict: Character frequency map {char: count}
    """
    char_freq = {}
    
    for char in s:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    return char_freq


def char_frequency_optimal(s):
    """
    Count character frequency using .get() method (Pythonic).
    
    Args:
        s (str): Input string
    
    Returns:
        dict: Character frequency map {char: count}
    """
    char_freq = {}
    
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1
    
    return char_freq


def char_frequency_array_based(s):
    """
    Count character frequency using array (for lowercase a-z only).
    
    Logic:
    - Create array of 26 zeros (one for each letter a-z)
    - For each character, calculate its index: ord(char) - ord('a')
    - Increment the count at that index
    
    Note: This only works for lowercase letters a-z.
    Other characters (spaces, uppercase, etc.) are ignored.
    
    Args:
        s (str): Input string (ideally lowercase letters only)
    
    Returns:
        list: Array of 26 integers representing counts for a-z
    """
    # Array for 26 lowercase letters (index 0 = 'a', index 25 = 'z')
    freq_array = [0] * 26
    
    for char in s:
        # Only process lowercase letters
        if 'a' <= char <= 'z':
            index = ord(char) - ord('a')  # Convert char to index (0-25)
            freq_array[index] += 1
    
    return freq_array


def query_character_frequency(freq_map, characters):
    """
    Query frequency of specific characters from a frequency map.
    
    Args:
        freq_map (dict): Pre-computed character frequency map
        characters (list): List of characters to query
    
    Returns:
        dict: Query results {char: count}
    """
    results = {}
    for char in characters:
        results[char] = freq_map.get(char, 0)
    return results


def print_char_frequency_array(freq_array):
    """
    Print character frequency from array in readable format.
    Only prints characters with count > 0.
    """
    print("  Character frequencies (array-based):")
    for i in range(26):
        if freq_array[i] > 0:
            char = chr(ord('a') + i)  # Convert index back to character
            print(f"    '{char}': {freq_array[i]}")


# Example Usage - Character Hashing
print("=" * 60)
print("SECTION 6: CHARACTER HASHING")
print("=" * 60)

s = "hello world"
query_chars = ['h', 'e', 'l', 'o', ' ', 'w', 'r', 'd']

print(f"String: \"{s}\"")
print(f"Characters to query: {query_chars}")
print()

# Method 1: Basic dictionary approach
char_freq_basic_result = char_frequency_basic(s)
print(f"Character Frequency (Basic Dict): {char_freq_basic_result}")

# Method 2: Optimal with .get()
char_freq_optimal_result = char_frequency_optimal(s)
print(f"Character Frequency (Optimal Dict): {char_freq_optimal_result}")

# Method 3: Array-based (lowercase only)
char_freq_array_result = char_frequency_array_based(s)
print(f"Character Frequency Array: {char_freq_array_result}")
print_char_frequency_array(char_freq_array_result)

# Query specific characters
print("\nQuerying specific characters:")
for char in query_chars:
    count = char_freq_optimal_result.get(char, 0)
    print(f"  Character '{char}' appears {count} times in \"{s}\"")
print()


# ==============================================================================
# SECTION 7: SUMMARY & KEY TAKEAWAYS
# ==============================================================================
"""
SUMMARY:
========

1. COUNTING DIGITS:
   - Iterative: O(d) time, O(1) space - divide by 10 repeatedly
   - Mathematical: O(1) time - use log10

2. PALINDROME:
   - String reversal: s[::-1] - simple and readable
   - Two-pointer: O(1) space - efficient for memory

3. ARMSTRONG NUMBER:
   - Sum of digits^(num_digits) = original number
   - Examples: 153, 370, 371, 407, 1634

4. FACTORIAL:
   - Iterative: O(n) time, O(1) space - use loop
   - Recursive: O(n) time, O(n) space - elegant but uses stack

5. HASHING CONCEPTS:
   - Pre-store data for O(1) lookup
   - Dictionary: Flexible, works with any hashable type
   - Array: Faster for small, known ranges
   - .get(key, default): Pythonic way to handle missing keys

6. CHARACTER HASHING:
   - Same as number hashing but for strings
   - ord(char): Get ASCII value of character
   - chr(num): Get character from ASCII value
   - Index formula: ord(char) - ord('a') for lowercase letters

TIME COMPLEXITY COMPARISON:
===========================
| Operation                  | Brute Force | With Hashing |
|---------------------------|-------------|--------------|
| Count frequency of 1 elem | O(n)        | O(1)         |
| Count all frequencies     | O(n²)       | O(n)         |
| Multiple queries          | O(n * q)    | O(n + q)     |

PYTHON TIPS USED:
================
- s[::-1]           -> Reverse string/list
- dict.get(k, 0)    -> Get value or default
- ord('a')          -> ASCII value (97)
- chr(97)           -> Character ('a')
- abs(n)            -> Absolute value
- len(str(n))       -> Count digits as string
"""

print("=" * 60)
print("PRACTICE COMPLETE!")
print("=" * 60)
print("Topics covered:")
print("  1. Counting Digits (Iterative & Mathematical)")
print("  2. Palindrome Check (Number & String)")
print("  3. Armstrong Number")
print("  4. Factorial (Iterative & Recursive)")
print("  5. Frequency Map / Hashing (Numbers)")
print("  6. Character Hashing")
print("=" * 60)





