"""
LeetCode #1104 - Path In Zigzag Labelled Binary Tree
Topic: Tree
Difficulty: Medium

PROBLEM EXPLANATION:
In a complete binary tree, nodes are labeled in zigzag order:
Row 1: left to right (1)
Row 2: right to left (3, 2)
Row 3: left to right (4, 5, 6, 7)
Row 4: right to left (15, 14, 13, 12, 11, 10, 9, 8)

Given a label, return the path from root to that label.

Example:
Input: label = 14
Output: [1,3,4,14]

APPROACH:
1. Find which row the label is in
2. Convert zigzag position to normal binary tree position
3. Get parent by dividing position by 2
4. Convert parent back to zigzag position
5. Repeat until reaching root

Time Complexity: O(log n)
Space Complexity: O(log n)
"""

def pathInZigZagTree(label):
    """
    Returns path from root to label in zigzag tree
    """
    # Find the row (level) of the label
    row = 0
    temp = label
    while temp > 0:
        temp //= 2
        row += 1
    
    path = []
    
    while label >= 1:
        path.append(label)
        
        # Get row range
        row_start = 2 ** (row - 1)
        row_end = 2 ** row - 1
        
        # Convert to normal position and get parent
        # In zigzag: reverse position in row
        normal_pos = row_start + row_end - label
        parent = normal_pos // 2
        
        # Move to parent row
        row -= 1
        
        if row > 0:
            # Convert parent back to zigzag
            parent_row_start = 2 ** (row - 1)
            parent_row_end = 2 ** row - 1
            label = parent_row_start + parent_row_end - parent
        else:
            label = 0
    
    return path[::-1]


# Test cases
if __name__ == "__main__":
    print(f"Test 1: {pathInZigZagTree(14)}")  # Expected: [1,3,4,14]
    print(f"Test 2: {pathInZigZagTree(26)}")  # Expected: [1,2,6,10,26]
    print(f"Test 3: {pathInZigZagTree(1)}")   # Expected: [1]
