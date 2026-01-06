"""

                 LeetCode #49 - Group Anagrams                                
                 Topic: String/HashMap | Difficulty: Medium                   
                 Company: Amazon, Meta, Microsoft                             


PROBLEM: Group strings that are anagrams of each other.

Example:
  ["eat","tea","tan","ate","nat","bat"]
   [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from collections import defaultdict

#  SOLUTION 1: Sort as Key (OPTIMAL for interview)
def groupAnagrams(strs):
    """
    Use sorted string as hash key
    Time: O(n * k log k), Space: O(n*k)
    where n=len(strs), k=max length of string
    
    Anagrams have same sorted form: "eat", "tea"  "aet"
    """
    groups = defaultdict(list)
    
    for s in strs:
        key = ''.join(sorted(s))
        groups[key].append(s)
    
    return list(groups.values())


#  SOLUTION 2: Character Count as Key (OPTIMAL time)
def groupAnagrams_count(strs):
    """
    Use character count tuple as key
    Time: O(n * k), Space: O(n*k)
    
    Faster than sorting: count each char a-z.
    """
    groups = defaultdict(list)
    
    for s in strs:
        # Count chars (26 letters)
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        # Use tuple as dict key
        groups[tuple(count)].append(s)
    
    return list(groups.values())


#  SOLUTION 3: Prime Product (Mathematical)
def groupAnagrams_prime(strs):
    """
    Use prime product as key
    Time: O(n * k), Space: O(n*k)
    
    Map each char to prime, multiply: anagrams have same product.
    """
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
    groups = defaultdict(list)
    
    for s in strs:
        key = 1
        for c in s:
            key *= primes[ord(c) - ord('a')]
        groups[key].append(s)
    
    return list(groups.values())


if __name__ == "__main__":
    print("Testing Group Anagrams:\n")
    
    strs = ["eat","tea","tan","ate","nat","bat"]
    
    r1 = groupAnagrams(strs)
    r2 = groupAnagrams_count(strs)
    r3 = groupAnagrams_prime(strs)
    
    print(f"Input: {strs}\n")
    print(f"Sort: {r1}")
    print(f"Count: {r2}")
    print(f"Prime: {r3}")
    print(f"\nAll have 3 groups: {len(r1) == len(r2) == len(r3) == 3} ")
