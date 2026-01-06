"""

              LeetCode #791 - Custom Sort String                              
              Topic: String/HashMap | Difficulty: Medium                      
              Company: Meta, Amazon                                           


PROBLEM: Sort string based on custom order defined by another string.

Example:
  order = "cba", s = "abcd"
   "cbad" (c first, then b, then a, then d)
"""

from collections import Counter

#  SOLUTION 1: Count and Build (OPTIMAL)
def customSortString(order, s):
    """
    Count chars in s, build result by order
    Time: O(n), Space: O(1) - max 26 chars
    
    Process order first, then remaining chars.
    """
    count = Counter(s)
    result = []
    
    # Add chars in order
    for char in order:
        if char in count:
            result.append(char * count[char])
            del count[char]
    
    # Add remaining chars
    for char in count:
        result.append(char * count[char])
    
    return ''.join(result)


#  SOLUTION 2: Custom Sort Key
def customSortString_sort(order, s):
    """
    Sort with custom key
    Time: O(n log n), Space: O(n)
    
    Use order index as sort key.
    """
    order_map = {char: i for i, char in enumerate(order)}
    
    # Chars not in order get high value
    return ''.join(sorted(s, key=lambda x: order_map.get(x, 100)))


#  SOLUTION 3: Bucket Sort
def customSortString_bucket(order, s):
    """
    Bucket sort approach
    Time: O(n), Space: O(1)
    
    Similar to counting sort.
    """
    buckets = {char: [] for char in order}
    extra = []
    
    for char in s:
        if char in buckets:
            buckets[char].append(char)
        else:
            extra.append(char)
    
    result = []
    for char in order:
        result.extend(buckets[char])
    result.extend(extra)
    
    return ''.join(result)


if __name__ == "__main__":
    print("Testing Custom Sort String:\n")
    
    tests = [
        ("cba", "abcd", "cbad"),
        ("bcafg", "abcd", "bcad")
    ]
    
    for order, s, expected in tests:
        r1 = customSortString(order, s)
        r2 = customSortString_sort(order, s)
        r3 = customSortString_bucket(order, s)
        
        print(f'order="{order}", s="{s}":')
        print(f'  Count={r1}, Sort={r2}, Bucket={r3}')
        print(f'  Expected={expected} {"" if r1 == expected else ""}\n')
