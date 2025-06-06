"""
LeetCode #139 - Word Break
Topic: Dynamic Programming / String
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Can string be segmented into dictionary words?

Example:
s = "leetcode", wordDict = ["leet","code"]
-> True ("leet" + "code")

Think of it like:
Can you split sentence using dictionary words?

WHY THIS WORKS (Simple Explanation):
DP: dp[i] = can we break s[0:i]?
For each position, check if any word ends there.

Time: O(n² × m) where m is avg word length
Space: O(n)
"""

def wordBreak(s, wordDict):
    """Check if string can be segmented"""
    wordSet = set(wordDict)
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Empty string
    
    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break
    
    return dp[n]


# Test
if __name__ == "__main__":
    tests = [
        ("leetcode", ["leet","code"], True),
        ("applepenapple", ["apple","pen"], True),
        ("catsandog", ["cats","dog","sand","and","cat"], False),
    ]
    
    for s, words, exp in tests:
        result = wordBreak(s, words)
        print(f'"{s}" -> {result} (expected {exp})')
