"""
LeetCode #979 - Distribute Coins in Binary Tree
Topic: Tree
Difficulty: Medium

PROBLEM EXPLANATION:
Given the root of a binary tree with n nodes where each node has some coins,
there are exactly n coins total. In one move, we can choose two adjacent nodes
and move one coin from one to the other. Return minimum number of moves required
to make every node have exactly one coin.

Example:
Input: root = [3,0,0]
Output: 2
Explanation: Move 2 coins from root to children

APPROACH (DFS - Post-order):
1. For each node, calculate excess/deficit coins
2. Excess = node.val + left_excess + right_excess - 1
3. Moves needed = |left_excess| + |right_excess|
4. Return excess to parent

Time Complexity: O(n)
Space Complexity: O(h)
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def distributeCoins(root):
    """
    Returns minimum moves to distribute coins
    """
    moves = [0]
    
    def dfs(node):
        if not node:
            return 0
        
        # Get excess coins from left and right subtrees
        left_excess = dfs(node.left)
        right_excess = dfs(node.right)
        
        # Moves needed = absolute value of excesses
        moves[0] += abs(left_excess) + abs(right_excess)
        
        # Return excess coins to parent
        # Current node has: node.val coins
        # Receives: left_excess + right_excess
        # Needs: 1 coin
        # Excess: node.val + left_excess + right_excess - 1
        return node.val + left_excess + right_excess - 1
    
    dfs(root)
    return moves[0]


# Test cases
if __name__ == "__main__":
    # Test 1: [3,0,0]
    root1 = TreeNode(3, TreeNode(0), TreeNode(0))
    print(f"Test 1: {distributeCoins(root1)}")  # Expected: 2
    
    # Test 2: [0,3,0]
    root2 = TreeNode(0, TreeNode(3), TreeNode(0))
    print(f"Test 2: {distributeCoins(root2)}")  # Expected: 3
    
    # Test 3: [1,0,2]
    root3 = TreeNode(1, TreeNode(0), TreeNode(2))
    print(f"Test 3: {distributeCoins(root3)}")  # Expected: 2
