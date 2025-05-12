"""
LeetCode #121 - Best Time to Buy and Sell Stock
Topic: Array
Difficulty: Easy

PROBLEM EXPLANATION (Easy Terms):
Buy stock on one day and sell on a future day to maximize profit.

Example:
[7,1,5,3,6,4] -> Buy at 1, sell at 6 -> profit = 5

Think of it like:
You have a time machine showing future prices.
Find the biggest difference between buy (lower) and sell (higher) days!

WHY THIS WORKS (Simple Explanation):
Track two things:
1. Minimum price seen so far (best day to buy)
2. Maximum profit possible (selling today vs best buy day)

For each day:
- Update minimum buy price
- Calculate profit if we sell today
- Update maximum profit

Like finding the lowest valley and highest peak after it!

Time Complexity: O(n) - single pass
Space Complexity: O(1) - only two variables
"""

def maxProfit(prices):
    """
    Find maximum profit from one buy and one sell
    
    Visual example: [7, 1, 5, 3, 6, 4]
    
    Day 0: price=7, min_price=7, max_profit=0
           (can't sell on first day)
    
    Day 1: price=1, min_price=1, profit=1-1=0, max_profit=0
           (found better buy price!)
    
    Day 2: price=5, min_price=1, profit=5-1=4, max_profit=4
           (if we bought at 1, selling at 5 gives 4)
    
    Day 3: price=3, min_price=1, profit=3-1=2, max_profit=4
    
    Day 4: price=6, min_price=1, profit=6-1=5, max_profit=5
           (best profit: buy at 1, sell at 6)
    
    Day 5: price=4, min_price=1, profit=4-1=3, max_profit=5
    
    Result: 5
    """
    if not prices:
        return 0
    
    # Track minimum price seen (best day to buy)
    min_price = prices[0]
    max_profit = 0
    
    for price in prices[1:]:
        # Calculate profit if we sell today
        profit = price - min_price
        
        # Update maximum profit
        max_profit = max(max_profit, profit)
        
        # Update minimum price (better buy day)
        min_price = min(min_price, price)
    
    return max_profit


def maxProfit_verbose(prices):
    """
    Same solution with detailed output for learning
    """
    if not prices:
        return 0
    
    min_price = prices[0]
    max_profit = 0
    best_buy_day = 0
    best_sell_day = 0
    
    print(f"Prices: {prices}\n")
    
    for i, price in enumerate(prices):
        profit = price - min_price
        
        print(f"Day {i}: price=${price}")
        print(f"  Min price so far: ${min_price}")
        print(f"  Profit if sell today: ${profit}")
        
        if profit > max_profit:
            max_profit = profit
            best_sell_day = i
            print(f"  NEW BEST PROFIT: ${max_profit} ✓")
        
        if price < min_price:
            min_price = price
            best_buy_day = i
            print(f"  NEW BEST BUY DAY: day {i} at ${price} ✓")
        
        print()
    
    print(f"Result: Buy on day {best_buy_day} at ${prices[best_buy_day]}, "
          f"sell on day {best_sell_day} at ${prices[best_sell_day]}")
    print(f"Profit: ${max_profit}\n")
    
    return max_profit


# Test cases
if __name__ == "__main__":
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),  # Buy at 1, sell at 6
        ([7, 6, 4, 3, 1], 0),     # Prices only decrease
        ([1, 2, 3, 4, 5], 4),     # Buy at 1, sell at 5
        ([2, 4, 1], 2),           # Buy at 2, sell at 4
        ([3, 2, 6, 5, 0, 3], 4),  # Buy at 2, sell at 6
    ]
    
    print("=== Testing Standard Solution ===")
    for prices, expected in test_cases:
        result = maxProfit(prices)
        status = "✓" if result == expected else "✗"
        print(f"{status} Prices: {prices}")
        print(f"   Max Profit: ${result} (Expected: ${expected})")
        print()
    
    print("=== Verbose Solution (Example) ===")
    maxProfit_verbose([7, 1, 5, 3, 6, 4])
