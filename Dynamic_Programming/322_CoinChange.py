"""
LeetCode #322 - Coin Change
Topic: Dynamic Programming
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
You have coins of different denominations and a target amount.
Find the MINIMUM number of coins needed to make that amount.
Return -1 if impossible.

Example:
coins = [1,2,5], amount = 11
Answer: 3 coins (5+5+1)

coins = [2], amount = 3
Answer: -1 (impossible with only 2-cent coins)

Think of it like:
Making change with fewest coins. Like at a store!

WHY THIS WORKS (Simple Explanation):
For each amount from 1 to target:
- Try using each coin
- If we use coin X, we need dp[amount - X] more coins
- Pick the option with minimum coins

Build up from smaller amounts to target!

Time Complexity: O(amount * coins)
Space Complexity: O(amount)
"""

def coinChange(coins, amount):
    """
    Find minimum coins needed using dynamic programming
    
    Visual example: coins=[1,2,5], amount=11
    
    dp[0] = 0 (need 0 coins for amount 0)
    dp[1] = 1 (use coin 1)
    dp[2] = 1 (use coin 2)
    dp[3] = 2 (use 2+1 or 1+1+1, min is 2)
    dp[4] = 2 (use 2+2)
    dp[5] = 1 (use coin 5)
    dp[6] = 2 (use 5+1)
    ...
    dp[11] = 3 (use 5+5+1)
    """
    # dp[i] = minimum coins needed for amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins for amount 0
    
    # Build up for each amount
    for amt in range(1, amount + 1):
        # Try each coin
        for coin in coins:
            if coin <= amt:
                # Use this coin + minimum for remaining amount
                dp[amt] = min(dp[amt], dp[amt - coin] + 1)
    
    # If still infinity, impossible
    return dp[amount] if dp[amount] != float('inf') else -1


def coinChange_verbose(coins, amount):
    """
    Detailed version showing the building process
    """
    print(f"Coins: {coins}")
    print(f"Target amount: {amount}")
    print("\nBuilding solution from 0 to target...\n")
    
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    print(f"Amount 0: Need 0 coins (base case)")
    
    for amt in range(1, amount + 1):
        print(f"\nAmount {amt}:")
        options = []
        
        for coin in coins:
            if coin <= amt:
                coins_needed = dp[amt - coin] + 1
                options.append((coin, coins_needed))
                print(f"  Use coin {coin}: need dp[{amt}-{coin}]+1 = {dp[amt-coin]}+1 = {coins_needed} coins")
                
                dp[amt] = min(dp[amt], coins_needed)
        
        if dp[amt] == float('inf'):
            print(f"  IMPOSSIBLE to make amount {amt}")
        else:
            # Find which coin gave minimum
            best_coin = min(options, key=lambda x: x[1])[0]
            print(f"  MINIMUM: {dp[amt]} coins (use coin {best_coin})")
    
    result = dp[amount] if dp[amount] != float('inf') else -1
    print(f"\nFinal answer: {result} coins")
    
    # Show one possible solution
    if result != -1:
        print(f"\nOne possible combination:")
        remaining = amount
        used_coins = []
        while remaining > 0:
            for coin in coins:
                if coin <= remaining and dp[remaining - coin] == dp[remaining] - 1:
                    used_coins.append(coin)
                    remaining -= coin
                    break
        print(f"  {' + '.join(map(str, used_coins))} = {amount}")
    
    return result


def coinChange_bfs(coins, amount):
    """
    Alternative: BFS approach (finds shortest path)
    
    Think of it as finding shortest path from 0 to amount
    """
    if amount == 0:
        return 0
    
    from collections import deque
    
    queue = deque([(0, 0)])  # (current_amount, num_coins)
    visited = {0}
    
    while queue:
        current_amt, num_coins = queue.popleft()
        
        # Try each coin
        for coin in coins:
            next_amt = current_amt + coin
            
            if next_amt == amount:
                return num_coins + 1
            
            if next_amt < amount and next_amt not in visited:
                visited.add(next_amt)
                queue.append((next_amt, num_coins + 1))
    
    return -1


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 5], 11, 3),
        ([2], 3, -1),
        ([1], 0, 0),
        ([1], 1, 1),
        ([1], 2, 2),
        ([1, 2, 5], 100, 20),
        ([186, 419, 83, 408], 6249, 20),
    ]
    
    print("=== Testing DP Solution ===")
    for coins, amount, expected in test_cases:
        result = coinChange(coins, amount)
        status = "✓" if result == expected else "✗"
        print(f"{status} coins={coins}, amount={amount}")
        print(f"   Min coins: {result} (Expected: {expected})")
        print()
    
    print("=== Testing BFS Solution ===")
    for coins, amount, expected in test_cases[:5]:  # Test smaller cases
        result = coinChange_bfs(coins, amount)
        status = "✓" if result == expected else "✗"
        print(f"{status} coins={coins}, amount={amount} -> {result}")
    
    print("\n" + "="*50)
    print("=== Verbose Example ===")
    coinChange_verbose([1, 2, 5], 11)
