"""
LeetCode #133 - Clone Graph
Topic: Graph / DFS
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Deep copy an undirected graph.

Think of it like:
Duplicating a network of connected nodes!

WHY THIS WORKS (Simple Explanation):
Use DFS with hashmap to track cloned nodes:
1. Clone current node
2. Recursively clone all neighbors
3. Store in map to avoid duplicates

Time: O(V + E)
Space: O(V)
"""

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


def cloneGraph(node):
    """Clone undirected graph"""
    if not node:
        return None
    
    clones = {}  # Map original -> clone
    
    def dfs(node):
        if node in clones:
            return clones[node]
        
        # Clone current node
        clone = Node(node.val)
        clones[node] = clone
        
        # Clone neighbors
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
        
        return clone
    
    return dfs(node)


# Test
if __name__ == "__main__":
    # Create graph: 1--2
    #               |  |
    #               4--3
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    
    cloned = cloneGraph(n1)
    print(f"Original node 1: {id(n1)}")
    print(f"Cloned node 1: {id(cloned)}")
    print(f"Different objects: {n1 is not cloned}")
