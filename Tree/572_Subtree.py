"""
LeetCode #572 - Subtree of Another Tree
Topic: Tree / DFS
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Check if subRoot is a subtree of root.

Think of it like:
Is this smaller tree contained in bigger tree?

WHY THIS WORKS (Simple Explanation):
For each node in root, check if identical to subRoot.

Time: O(m × n)
Space: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSubtree(root, subRoot):
    """Check if subRoot is subtree of root"""
    if not root:
        return False
    
    if isSameTree(root, subRoot):
        return True
    
    return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def isSameTree(p, q):
    """Check if two trees are identical"""
    if not p and not q:
        return True
    if not p or not q:
        return False
    
    return (p.val == q.val and 
            isSameTree(p.left, q.left) and 
            isSameTree(p.right, q.right))


# Test
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(4, TreeNode(1), TreeNode(2))
    root.right = TreeNode(5)
    
    sub = TreeNode(4, TreeNode(1), TreeNode(2))
    
    print(f"Is subtree: {isSubtree(root, sub)}")  # True
