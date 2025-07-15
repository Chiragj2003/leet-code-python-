"""
LeetCode #763 - Partition Labels
Topic: Greedy / String
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Partition string so each letter appears in at most one part.
Maximize number of parts.

Example:
"ababcbacadefegdehijhklij" -> [9,7,8]
("ababcbaca", "defegde", "hijhklij")

Think of it like:
Splitting string into independent segments!

WHY THIS WORKS:
Track last occurrence of each character.
Extend partition to include all occurrences.

Time: O(n)
Space: O(1) - at most 26 letters
"""

def partitionLabels(s):
    """Partition string into max parts"""
    last = {c: i for i, c in enumerate(s)}
    
    partitions = []
    start = end = 0
    
    for i, c in enumerate(s):
        end = max(end, last[c])
        
        if i == end:
            partitions.append(end - start + 1)
            start = i + 1
    
    return partitions


# Test
if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"
    result = partitionLabels(s)
    print(f'"{s}" -> {result}')
