"""
LeetCode #457 - Circular Array Loop
Topic: Two Pointers
Difficulty: Medium

PROBLEM EXPLANATION:
Given a circular array of non-zero integers, determine if there exists a cycle.
A cycle must:
1. Follow one direction (all forward or all backward)
2. Have length > 1
3. Each move is determined by the value at current position

Example:
Input: nums = [2,-1,1,2,2]
Output: true
Explanation: There is a cycle from index 0 -> 2 -> 3 -> 0

APPROACH (Fast & Slow Pointers):
1. Try starting from each index
2. Use slow and fast pointers (like detecting cycle in linked list)
3. Check if all moves in the cycle go in the same direction
4. Mark visited indices to avoid revisiting

Time Complexity: O(n²)
Space Complexity: O(1)
"""

def circularArrayLoop(nums):
    """
    Returns True if there exists a valid cycle
    """
    n = len(nums)
    
    def getNext(index):
        """Get next index in circular array"""
        return (index + nums[index]) % n
    
    for i in range(n):
        if nums[i] == 0:
            continue
        
        # Initialize slow and fast pointers
        slow = fast = i
        forward = nums[i] > 0  # Direction of cycle
        
        while True:
            # Move slow pointer one step
            slow = getNext(slow)
            
            # Check if direction changes or single element cycle
            if nums[slow] == 0 or (nums[slow] > 0) != forward:
                break
            if slow == getNext(slow):  # Single element cycle
                break
            
            # Move fast pointer two steps
            fast = getNext(fast)
            if nums[fast] == 0 or (nums[fast] > 0) != forward:
                break
            if fast == getNext(fast):  # Single element cycle
                break
            
            fast = getNext(fast)
            if nums[fast] == 0 or (nums[fast] > 0) != forward:
                break
            
            # Check if slow and fast meet (cycle found)
            if slow == fast:
                return True
        
        # Mark all elements in this path as visited
        slow = i
        forward = nums[i] > 0
        while nums[slow] != 0 and (nums[slow] > 0) == forward:
            next_slow = getNext(slow)
            nums[slow] = 0
            slow = next_slow
    
    return False


# Test cases
if __name__ == "__main__":
    test1 = [2, -1, 1, 2, 2]
    print(f"Test 1: {circularArrayLoop(test1)}")  # Expected: True
    
    test2 = [-1, 2]
    print(f"Test 2: {circularArrayLoop(test2)}")  # Expected: False
    
    test3 = [-2, 1, -1, -2, -2]
    print(f"Test 3: {circularArrayLoop(test3)}")  # Expected: False
