"""
LeetCode #637 - Average of Levels in Binary Tree
Topic: Tree
Difficulty: Easy

PROBLEM EXPLANATION:
Given the root of a binary tree, return the average value of nodes
on each level as an array.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: Level 0: 3, Level 1: (9+20)/2, Level 2: (15+7)/2

APPROACH (BFS - Level Order Traversal):
1. Use queue for level-order traversal
2. Process each level separately
3. Calculate average for each level

Time Complexity: O(n)
Space Complexity: O(w) where w is max width
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def averageOfLevels(root):
    """
    Returns list of average values at each level
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_sum = 0
        level_count = len(queue)
        
        # Process all nodes at current level
        for _ in range(level_count):
            node = queue.popleft()
            level_sum += node.val
            
            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Calculate average for this level
        result.append(level_sum / level_count)
    
    return result


# Test cases
if __name__ == "__main__":
    # Test: [3,9,20,null,null,15,7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20, TreeNode(15), TreeNode(7))
    
    print(f"Test: {averageOfLevels(root)}")
    # Expected: [3.0, 14.5, 11.0]
