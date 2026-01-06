"""LeetCode #134 - Gas Station | Greedy | Medium"""

def canCompleteCircuit(gas, cost):
    """ OPTIMAL - One Pass Greedy: O(n) time, O(1) space"""
    if sum(gas) < sum(cost):
        return -1
    
    start = total_tank = 0
    for i in range(len(gas)):
        total_tank += gas[i] - cost[i]
        if total_tank < 0:
            start = i + 1
            total_tank = 0
    
    return start

def canCompleteCircuit_brute(gas, cost):
    """ SOLUTION 2 - Brute Force: O(n) time, O(1) space"""
    n = len(gas)
    for start in range(n):
        tank = 0
        valid = True
        for i in range(n):
            idx = (start + i) % n
            tank += gas[idx] - cost[idx]
            if tank < 0:
                valid = False
                break
        if valid:
            return start
    return -1

if __name__ == "__main__":
    tests = [([1,2,3,4,5], [3,4,5,1,2], 3), ([2,3,4], [3,4,3], -1)]
    print("Testing Gas Station:")
    for gas, cost, exp in tests:
        r1, r2 = canCompleteCircuit(gas, cost), canCompleteCircuit_brute(gas, cost)
        print(f"gas={gas}, cost={cost}: Greedy={r1} Brute={r2} (exp={exp})")
