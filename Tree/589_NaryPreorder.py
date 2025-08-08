"""
LeetCode #589 - N-ary Tree Preorder Traversal
Topic: Tree
Difficulty: Easy

PROBLEM EXPLANATION:
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.
Preorder: root -> children (left to right)

Example:
Input: root = [1,null,3,2,4,null,5,6]
Output: [1,3,5,6,2,4]

APPROACH (Recursive):
1. Visit root
2. Recursively visit each child from left to right

Time Complexity: O(n)
Space Complexity: O(h)
"""

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


def preorder(root):
    """
    Returns preorder traversal of n-ary tree
    """
    result = []
    
    def dfs(node):
        if not node:
            return
        
        # Visit root
        result.append(node.val)
        
        # Visit children
        for child in node.children:
            dfs(child)
    
    dfs(root)
    return result


# Iterative approach
def preorder_iterative(root):
    """
    Iterative approach using stack
    """
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.val)
        
        # Add children in reverse order (so left is processed first)
        for child in reversed(node.children):
            stack.append(child)
    
    return result


# Test cases
if __name__ == "__main__":
    # Test: [1,null,3,2,4,null,5,6]
    root = Node(1)
    child3 = Node(3, [Node(5), Node(6)])
    child2 = Node(2)
    child4 = Node(4)
    root.children = [child3, child2, child4]
    
    print(f"Test recursive: {preorder(root)}")  # Expected: [1,3,5,6,2,4]
    print(f"Test iterative: {preorder_iterative(root)}")  # Expected: [1,3,5,6,2,4]
