"""
LeetCode #1022 - Sum of Root To Leaf Binary Numbers
Topic: Tree
Difficulty: Easy

PROBLEM EXPLANATION:
Given a binary tree where each node contains 0 or 1, each root-to-leaf path
represents a binary number. Return the sum of all these numbers.

Example:
Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: 
Path 100 = 4
Path 101 = 5
Path 110 = 6
Path 111 = 7
Sum = 22

APPROACH (DFS):
1. Traverse tree keeping track of current binary number
2. At each node: current_num = current_num * 2 + node.val
3. When reaching leaf, add to sum
4. Backtrack and try other paths

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sumRootToLeaf(root):
    """
    Returns sum of all root-to-leaf binary numbers
    """
    def dfs(node, current_num):
        if not node:
            return 0
        
        # Update current binary number
        current_num = current_num * 2 + node.val
        
        # If leaf node, return the number
        if not node.left and not node.right:
            return current_num
        
        # Sum from left and right subtrees
        return dfs(node.left, current_num) + dfs(node.right, current_num)
    
    return dfs(root, 0)


# Test cases
if __name__ == "__main__":
    # Test 1: [1,0,1,0,1,0,1]
    root1 = TreeNode(1)
    root1.left = TreeNode(0, TreeNode(0), TreeNode(1))
    root1.right = TreeNode(1, TreeNode(0), TreeNode(1))
    print(f"Test 1: {sumRootToLeaf(root1)}")  # Expected: 22
    
    # Test 2: [0]
    root2 = TreeNode(0)
    print(f"Test 2: {sumRootToLeaf(root2)}")  # Expected: 0
    
    # Test 3: [1]
    root3 = TreeNode(1)
    print(f"Test 3: {sumRootToLeaf(root3)}")  # Expected: 1
