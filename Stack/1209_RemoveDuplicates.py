"""
LeetCode #1209 - Remove All Adjacent Duplicates in String II
Topic: Stack
Difficulty: Medium

PROBLEM EXPLANATION:
Given a string s and an integer k, repeatedly remove k consecutive
equal characters. If multiple choices, remove the leftmost group.
Continue until no more removals are possible.

Example:
Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation:
1. Remove "eee" -> "ddbcccbdaa"
2. Remove "ccc" -> "ddbbbdaa"
3. Remove "bbb" -> "dddaa"
4. Remove "ddd" -> "aa"

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"

APPROACH (Stack with Count):
1. Use stack to store [character, count] pairs
2. For each character:
   - If it matches stack top, increment count
   - If count reaches k, remove from stack
   - Otherwise, push new [char, 1]
3. Reconstruct string from stack

Time Complexity: O(n)
Space Complexity: O(n)
"""

def removeDuplicates(s, k):
    """
    Returns string after removing k consecutive duplicates
    """
    stack = []  # Each element is [char, count]
    
    for char in s:
        if stack and stack[-1][0] == char:
            # Same character as top, increment count
            stack[-1][1] += 1
            
            # If count reaches k, remove the group
            if stack[-1][1] == k:
                stack.pop()
        else:
            # Different character, push new entry
            stack.append([char, 1])
    
    # Reconstruct string from stack
    result = []
    for char, count in stack:
        result.append(char * count)
    
    return ''.join(result)


# Test cases
if __name__ == "__main__":
    test1 = "deeedbbcccbdaa"
    print(f"Test 1: {removeDuplicates(test1, 3)}")
    # Expected: "aa"
    
    test2 = "pbbcggttciiippooaais"
    print(f"Test 2: {removeDuplicates(test2, 2)}")
    # Expected: "ps"
    
    test3 = "abcd"
    print(f"Test 3: {removeDuplicates(test3, 2)}")
    # Expected: "abcd"
    
    test4 = "aaabbbccc"
    print(f"Test 4: {removeDuplicates(test4, 3)}")
    # Expected: ""
