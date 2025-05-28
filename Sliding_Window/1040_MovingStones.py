"""
LeetCode #1040 - Moving Stones Until Consecutive II
Topic: Sliding Window / Two Pointers
Difficulty: Medium

PROBLEM EXPLANATION:
Given an integer array stones sorted in ascending order representing
positions of stones on a line. Move stones to make them consecutive.
In each move, pick a stone at an endpoint and move it to an unoccupied position.
Return [minimum_moves, maximum_moves].

Example:
Input: stones = [7,4,9]
Output: [1,2]
Explanation: Min: Move 4 to 8 -> [7,8,9]. Max: Move 4 to 10, then 10 to 8.

APPROACH:
Maximum moves: Move all stones from one side
Minimum moves: Use sliding window to find position where most stones fit

Time Complexity: O(n log n)
Space Complexity: O(1)
"""

def numMovesStonesII(stones):
    """
    Returns [minimum_moves, maximum_moves]
    """
    stones.sort()
    n = len(stones)
    
    # Maximum moves: fill gaps from one end
    # We can move stones from one end to fill gaps
    max_moves = max(stones[-1] - stones[1] - (n - 2),
                    stones[-2] - stones[0] - (n - 2))
    
    # Minimum moves: sliding window
    min_moves = n
    j = 0
    
    for i in range(n):
        # Expand window while stones fit in n positions
        while j < n and stones[j] - stones[i] + 1 <= n:
            j += 1
        
        # Number of stones in window
        stones_in_window = j - i
        
        # Special case: n-1 stones consecutive with 1 gap
        if stones_in_window == n - 1 and stones[j-1] - stones[i] == n - 2:
            min_moves = min(min_moves, 2)
        else:
            min_moves = min(min_moves, n - stones_in_window)
    
    return [min_moves, max_moves]


# Test cases
if __name__ == "__main__":
    print(f"Test 1: {numMovesStonesII([7,4,9])}")  # Expected: [1,2]
    print(f"Test 2: {numMovesStonesII([6,5,4,3,10])}")  # Expected: [2,3]
    print(f"Test 3: {numMovesStonesII([100,101,104,102,103])}")  # Expected: [0,0]
