"""
LeetCode #925 - Long Pressed Name
Topic: Two Pointers
Difficulty: Easy

PROBLEM EXPLANATION:
Your friend is typing their name on a keyboard. Sometimes, when typing a character,
the key might get long pressed and the character appears more than once.
Check if the typed string could be a result of long-pressing the name.

Example:
Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in typed were long pressed

Input: name = "saeed", typed = "ssaaedd"
Output: false
Explanation: 'e' must appear twice, but 'd' appears twice instead of 'e'

APPROACH (Two Pointers):
1. Use two pointers, one for name and one for typed
2. If characters match, move both pointers
3. If they don't match but typed[j] == typed[j-1], it's a long press - move typed pointer
4. Otherwise, it's invalid
5. Ensure all characters in name are processed

Time Complexity: O(n + m)
Space Complexity: O(1)
"""

def isLongPressedName(name, typed):
    """
    Returns True if typed could be a result of long-pressing name
    """
    i = 0  # pointer for name
    j = 0  # pointer for typed
    
    while j < len(typed):
        if i < len(name) and name[i] == typed[j]:
            # Characters match, move both pointers
            i += 1
            j += 1
        elif j > 0 and typed[j] == typed[j - 1]:
            # Long press detected (same as previous character)
            j += 1
        else:
            # Mismatch and not a long press
            return False
    
    # Check if all characters in name were processed
    return i == len(name)


# Test cases
if __name__ == "__main__":
    test1 = isLongPressedName("alex", "aaleex")
    print(f"Test 1: {test1}")  # Expected: True
    
    test2 = isLongPressedName("saeed", "ssaaedd")
    print(f"Test 2: {test2}")  # Expected: False
    
    test3 = isLongPressedName("leelee", "lleeelee")
    print(f"Test 3: {test3}")  # Expected: True
    
    test4 = isLongPressedName("alex", "aaleelx")
    print(f"Test 4: {test4}")  # Expected: False
    
    test5 = isLongPressedName("alex", "aaleexa")
    print(f"Test 5: {test5}")  # Expected: False
