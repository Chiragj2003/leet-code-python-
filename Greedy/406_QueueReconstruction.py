"""
LeetCode #406 - Queue Reconstruction by Height
Topic: Greedy / Sorting
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
People in queue: [height, k]
k = number of people >= height in front

Reconstruct queue!

Example:
[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
-> [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

Think of it like:
Arranging people by height and position!

WHY THIS WORKS (Simple Explanation):
1. Sort by height (desc), then by k (asc)
2. Insert each person at index k

Taller people first, then slot shorter ones!

Time: O(n²)
Space: O(n)
"""

def reconstructQueue(people):
    """Reconstruct queue by height"""
    # Sort: height desc, k asc
    people.sort(key=lambda x: (-x[0], x[1]))
    
    result = []
    for person in people:
        result.insert(person[1], person)
    
    return result


# Test
if __name__ == "__main__":
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    result = reconstructQueue(people)
    print(f"Reconstructed: {result}")
