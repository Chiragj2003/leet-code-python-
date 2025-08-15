"""
LeetCode #993 - Cousins in Binary Tree
Topic: Tree
Difficulty: Easy

PROBLEM EXPLANATION:
Two nodes are cousins if they have the same depth but different parents.
Given a binary tree and two node values x and y, return true if they are cousins.

Example:
Input: root = [1,2,3,4], x = 4, y = 3
Output: false (different depths)

Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
Output: true (same depth, different parents)

APPROACH (BFS with Level Order):
1. Use BFS to traverse level by level
2. Track parent and depth for both x and y
3. Check if same depth and different parents

Time Complexity: O(n)
Space Complexity: O(w) where w is max width
"""

from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isCousins(root, x, y):
    """
    Returns True if x and y are cousins
    """
    if not root:
        return False
    
    queue = deque([(root, None, 0)])  # (node, parent, depth)
    x_info = None
    y_info = None
    
    while queue:
        node, parent, depth = queue.popleft()
        
        # Check if we found x or y
        if node.val == x:
            x_info = (parent, depth)
        if node.val == y:
            y_info = (parent, depth)
        
        # If we found both, check if they're cousins
        if x_info and y_info:
            return x_info[1] == y_info[1] and x_info[0] != y_info[0]
        
        # Add children
        if node.left:
            queue.append((node.left, node, depth + 1))
        if node.right:
            queue.append((node.right, node, depth + 1))
    
    return False


# Alternative: DFS approach
def isCousins_dfs(root, x, y):
    """
    DFS approach
    """
    def dfs(node, parent, depth, target):
        if not node:
            return None
        if node.val == target:
            return (parent, depth)
        
        left = dfs(node.left, node, depth + 1, target)
        if left:
            return left
        return dfs(node.right, node, depth + 1, target)
    
    x_info = dfs(root, None, 0, x)
    y_info = dfs(root, None, 0, y)
    
    if not x_info or not y_info:
        return False
    
    return x_info[1] == y_info[1] and x_info[0] != y_info[0]


# Test cases
if __name__ == "__main__":
    # Test 1: [1,2,3,4]
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(4))
    root1.right = TreeNode(3)
    print(f"Test 1: {isCousins(root1, 4, 3)}")  # Expected: False
    
    # Test 2: [1,2,3,null,4,null,5]
    root2 = TreeNode(1)
    root2.left = TreeNode(2, None, TreeNode(4))
    root2.right = TreeNode(3, None, TreeNode(5))
    print(f"Test 2: {isCousins(root2, 5, 4)}")  # Expected: True
