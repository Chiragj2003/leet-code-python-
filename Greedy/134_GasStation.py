"""
LeetCode #134 - Gas Station
Topic: Greedy
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Circular route with gas stations.
Can you complete the circuit?

Example:
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
Start at index 3 -> Yes!

Think of it like:
Road trip - do you have enough fuel?

WHY THIS WORKS (Simple Explanation):
If total gas < total cost, impossible!
Otherwise, find starting point where gas never negative.

Time: O(n)
Space: O(1)
"""

def canCompleteCircuit(gas, cost):
    """Find starting gas station for complete circuit"""
    if sum(gas) < sum(cost):
        return -1
    
    start = 0
    tank = 0
    
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        
        if tank < 0:
            start = i + 1
            tank = 0
    
    return start


# Test
if __name__ == "__main__":
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    result = canCompleteCircuit(gas, cost)
    print(f"Start at station: {result}")
