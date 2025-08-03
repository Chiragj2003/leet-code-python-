"""
LeetCode #739 - Daily Temperatures
Topic: Hashmap / Stack (Monotonic Stack)
Difficulty: Medium

PROBLEM EXPLANATION:
Given an array of daily temperatures, return an array where answer[i] is
the number of days you have to wait after the i-th day to get a warmer temperature.
If there is no future day with warmer temperature, answer[i] = 0.

Example:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Explanation: 
- Day 0 (73°): Next warmer is day 1 (74°) -> wait 1 day
- Day 1 (74°): Next warmer is day 2 (75°) -> wait 1 day
- Day 2 (75°): Next warmer is day 6 (76°) -> wait 4 days
- Day 6 (76°): No warmer day -> 0

APPROACH (Monotonic Stack):
1. Use a stack to store indices of days
2. For each day, while current temp > temp at stack top:
   - Pop from stack (found warmer day for that index)
   - Calculate days difference
3. Push current day to stack
4. Stack maintains decreasing temperatures

Time Complexity: O(n)
Space Complexity: O(n)
"""

def dailyTemperatures(temperatures):
    """
    Returns array of days to wait for warmer temperature
    """
    n = len(temperatures)
    answer = [0] * n
    stack = []  # Store indices
    
    for i in range(n):
        # While current temp is warmer than temp at stack top
        while stack and temperatures[i] > temperatures[stack[-1]]:
            prev_index = stack.pop()
            answer[prev_index] = i - prev_index
        
        # Push current index
        stack.append(i)
    
    return answer


# Test cases
if __name__ == "__main__":
    test1 = [73, 74, 75, 71, 69, 72, 76, 73]
    print(f"Test 1: {dailyTemperatures(test1)}")
    # Expected: [1, 1, 4, 2, 1, 1, 0, 0]
    
    test2 = [30, 40, 50, 60]
    print(f"Test 2: {dailyTemperatures(test2)}")
    # Expected: [1, 1, 1, 0]
    
    test3 = [30, 60, 90]
    print(f"Test 3: {dailyTemperatures(test3)}")
    # Expected: [1, 1, 0]
    
    test4 = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    print(f"Test 4: {dailyTemperatures(test4)}")
    # Expected: [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
