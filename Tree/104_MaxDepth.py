"""
LeetCode #104 - Maximum Depth of Binary Tree
Topic: Tree (DFS/BFS)
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Find the maximum depth (height) of a binary tree.

Example:
    3
   / \
  9  20
     / \
    15  7

Depth = 3 (root -> 20 -> 15 or 7)

Think of it like:
Count the longest path from root to any leaf.
Like counting floors in a building from ground to top!

WHY THIS WORKS (Simple Explanation):
Two approaches:

1. RECURSIVE (DFS):
   - If node is None, depth is 0
   - Otherwise: 1 + max(left depth, right depth)
   - Like asking each subtree "how deep are you?"

2. ITERATIVE (BFS):
   - Process tree level by level
   - Count how many levels we process
   - Like counting floors as we go up!

Time Complexity: O(n) - visit every node
Space Complexity: O(h) for recursion, O(w) for BFS (h=height, w=max width)
"""

from collections import deque

class TreeNode:
    """Definition for a binary tree node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    """
    Recursive DFS solution
    
    Visual example:
        3
       / \
      9  20
         / \
        15  7
    
    maxDepth(3):
      left = maxDepth(9) = 1
      right = maxDepth(20):
        left = maxDepth(15) = 1
        right = maxDepth(7) = 1
        return 1 + max(1, 1) = 2
      return 1 + max(1, 2) = 3
    """
    # Base case: empty tree
    if not root:
        return 0
    
    # Recursive case: 1 + max of subtree depths
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)
    
    return 1 + max(left_depth, right_depth)


def maxDepth_iterative(root):
    """
    Iterative BFS solution using queue
    
    Process tree level by level:
    Level 1: [3] -> depth = 1
    Level 2: [9, 20] -> depth = 2
    Level 3: [15, 7] -> depth = 3
    
    Return final depth count
    """
    if not root:
        return 0
    
    # Queue for BFS: (node, depth)
    queue = deque([root])
    depth = 0
    
    # Process level by level
    while queue:
        depth += 1
        level_size = len(queue)
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            
            # Add children for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return depth


def maxDepth_dfs_stack(root):
    """
    Iterative DFS using stack
    
    Track (node, depth) pairs
    Keep maximum depth seen
    """
    if not root:
        return 0
    
    # Stack: (node, current_depth)
    stack = [(root, 1)]
    max_depth = 0
    
    while stack:
        node, depth = stack.pop()
        
        # Update max depth
        max_depth = max(max_depth, depth)
        
        # Add children with depth + 1
        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))
    
    return max_depth


# Helper function to create tree
def create_tree(values):
    """Create binary tree from level-order list (None for missing nodes)"""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        # Left child
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        # Right child
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
        ([], 0),
        ([0], 1),
        ([1, 2, 3, 4, 5], 3),
    ]
    
    print("=== Testing Recursive DFS ===")
    for values, expected in test_cases:
        root = create_tree(values)
        result = maxDepth(root)
        status = "✓" if result == expected else "✗"
        print(f"{status} Tree: {values}")
        print(f"   Depth: {result} (Expected: {expected})")
        print()
    
    print("=== Testing Iterative BFS ===")
    for values, expected in test_cases:
        root = create_tree(values)
        result = maxDepth_iterative(root)
        status = "✓" if result == expected else "✗"
        print(f"{status} Tree: {values}")
        print(f"   Depth: {result} (Expected: {expected})")
        print()
    
    print("=== Testing Iterative DFS ===")
    for values, expected in test_cases:
        root = create_tree(values)
        result = maxDepth_dfs_stack(root)
        status = "✓" if result == expected else "✗"
        print(f"{status} Tree: {values}")
        print(f"   Depth: {result} (Expected: {expected})")
        print()
