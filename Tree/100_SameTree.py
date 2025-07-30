"""
LeetCode #100 - Same Tree
Topic: Tree (DFS)
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Check if two binary trees are identical (same structure and values).

Example:
Tree 1:     Tree 2:
   1           1
  / \         / \
 2   3       2   3
-> True (identical)

Tree 1:     Tree 2:
   1           1
  /             \
 2               2
-> False (different structure)

Think of it like:
Compare two family trees - same people in same positions?

WHY THIS WORKS (Simple Explanation):
Recursively compare:
1. If both None -> identical (base case)
2. If one None -> not identical
3. If values different -> not identical
4. Check left subtrees AND right subtrees

Like checking if two puzzles are the same piece by piece!

Time Complexity: O(n) - visit each node once
Space Complexity: O(h) - recursion depth (h = height)
"""

class TreeNode:
    """Definition for a binary tree node"""
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    """
    Check if two trees are identical
    
    Visual example:
    Tree p:     Tree q:
       1           1
      / \         / \
     2   3       2   3
    
    isSameTree(1, 1):
      values match (1 == 1) ✓
      left: isSameTree(2, 2):
        values match (2 == 2) ✓
        left: isSameTree(None, None) -> True ✓
        right: isSameTree(None, None) -> True ✓
        return True
      right: isSameTree(3, 3):
        values match (3 == 3) ✓
        left: isSameTree(None, None) -> True ✓
        right: isSameTree(None, None) -> True ✓
        return True
      return True
    """
    # Both None - identical
    if not p and not q:
        return True
    
    # One None, one not - not identical
    if not p or not q:
        return False
    
    # Values must match
    if p.val != q.val:
        return False
    
    # Recursively check left and right subtrees
    return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


def isSameTree_iterative(p, q):
    """
    Iterative approach using stack
    
    Process pairs of nodes together
    Check each pair has matching values and structure
    """
    # Stack of node pairs to compare
    stack = [(p, q)]
    
    while stack:
        node1, node2 = stack.pop()
        
        # Both None - continue
        if not node1 and not node2:
            continue
        
        # One None - not same
        if not node1 or not node2:
            return False
        
        # Values differ - not same
        if node1.val != node2.val:
            return False
        
        # Add children to check
        stack.append((node1.left, node2.left))
        stack.append((node1.right, node2.right))
    
    return True


# Helper function
from collections import deque

def create_tree(values):
    """Create binary tree from level-order list"""
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    
    while queue and i < len(values):
        node = queue.popleft()
        
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    
    return root


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        ([], [], True),
        ([1], [1], True),
        ([1, 2], [1, 2], True),
    ]
    
    print("=== Testing Recursive Solution ===")
    for p_vals, q_vals, expected in test_cases:
        p = create_tree(p_vals)
        q = create_tree(q_vals)
        result = isSameTree(p, q)
        
        status = "✓" if result == expected else "✗"
        print(f"{status} Tree p: {p_vals}")
        print(f"   Tree q: {q_vals}")
        print(f"   Same: {result} (Expected: {expected})")
        print()
    
    print("=== Testing Iterative Solution ===")
    for p_vals, q_vals, expected in test_cases:
        p = create_tree(p_vals)
        q = create_tree(q_vals)
        result = isSameTree_iterative(p, q)
        
        status = "✓" if result == expected else "✗"
        print(f"{status} Tree p: {p_vals}")
        print(f"   Tree q: {q_vals}")
        print(f"   Same: {result} (Expected: {expected})")
        print()
