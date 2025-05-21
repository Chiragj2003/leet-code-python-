"""
LeetCode #338 - Counting Bits
Topic: Bit Manipulation / Dynamic Programming
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
For each number 0 to n, count number of 1's in binary representation.

Example:
n = 5 -> [0,1,1,2,1,2]
(0=0, 1=1, 2=10, 3=11, 4=100, 5=101)

Think of it like:
Counting set bits for range of numbers!

WHY THIS WORKS:
DP: bits[i] = bits[i >> 1] + (i & 1)
(Half the number + last bit)

Time: O(n)
Space: O(n)
"""

def countBits(n):
    """Count bits for 0 to n"""
    result = [0] * (n + 1)
    
    for i in range(1, n + 1):
        result[i] = result[i >> 1] + (i & 1)
    
    return result


# Test
if __name__ == "__main__":
    for n in [2, 5]:
        result = countBits(n)
        print(f"n={n}: {result}")
