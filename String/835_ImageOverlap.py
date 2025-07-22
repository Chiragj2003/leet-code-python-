"""
LeetCode #835 - Image Overlap
Topic: String / Array
Difficulty: Medium

PROBLEM EXPLANATION:
Given two binary matrices img1 and img2, translate one image to overlap
with the other. Return the largest possible overlap (number of 1s overlapping).

Example:
Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: Slide img1 to overlap maximum 1s with img2

APPROACH:
1. Find all positions of 1s in both images
2. For each pair of 1s, calculate the translation vector
3. Count occurrences of each translation vector
4. Maximum count is the answer

Time Complexity: O(n⁴)
Space Complexity: O(n²)
"""

from collections import Counter

def largestOverlap(img1, img2):
    """
    Returns maximum overlap count
    """
    n = len(img1)
    
    # Find all 1s positions
    ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j] == 1]
    ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j] == 1]
    
    if not ones1 or not ones2:
        return 0
    
    # Count translation vectors
    translations = Counter()
    
    for i1, j1 in ones1:
        for i2, j2 in ones2:
            # Translation needed to align (i1,j1) with (i2,j2)
            translation = (i2 - i1, j2 - j1)
            translations[translation] += 1
    
    return max(translations.values())


# Test cases
if __name__ == "__main__":
    test1_img1 = [[1,1,0],[0,1,0],[0,1,0]]
    test1_img2 = [[0,0,0],[0,1,1],[0,0,1]]
    print(f"Test 1: {largestOverlap(test1_img1, test1_img2)}")  # Expected: 3
    
    test2_img1 = [[1]]
    test2_img2 = [[1]]
    print(f"Test 2: {largestOverlap(test2_img1, test2_img2)}")  # Expected: 1
