"""

              LeetCode #835 - Image Overlap                                   
              Topic: Array/Math | Difficulty: Medium                          
              Company: Google                                                 


PROBLEM: Find max overlap of 1s when sliding one binary matrix over another.

Example:
  img1 = [[1,1,0],[0,1,0],[0,1,0]]
  img2 = [[0,0,0],[0,1,1],[0,0,1]]
   3 (overlap 3 ones)
"""

from collections import Counter

#  SOLUTION 1: Translation Vector (OPTIMAL)
def largestOverlap(img1, img2):
    """
    Count translation vectors between 1-positions
    Time: O(n), Space: O(n)
    where n=matrix dimension
    
    For each pair of 1s, compute translation vector.
    """
    n = len(img1)
    
    # Find all 1-positions
    ones1 = [(i, j) for i in range(n) for j in range(n) if img1[i][j]]
    ones2 = [(i, j) for i in range(n) for j in range(n) if img2[i][j]]
    
    if not ones1 or not ones2:
        return 0
    
    # Count translation vectors
    translations = Counter()
    
    for i1, j1 in ones1:
        for i2, j2 in ones2:
            # Vector from (i2,j2) to (i1,j1)
            delta = (i1 - i2, j1 - j2)
            translations[delta] += 1
    
    return max(translations.values())


#  SOLUTION 2: Brute Force Sliding
def largestOverlap_slide(img1, img2):
    """
    Try all possible translations
    Time: O(n), Space: O(1)
    
    Slide img2 over img1 in all directions.
    """
    n = len(img1)
    max_overlap = 0
    
    def count_overlap(dx, dy):
        count = 0
        for i in range(n):
            for j in range(n):
                i2, j2 = i + dx, j + dy
                if 0 <= i2 < n and 0 <= j2 < n:
                    if img1[i][j] == 1 and img2[i2][j2] == 1:
                        count += 1
        return count
    
    # Try all translations
    for dx in range(-n+1, n):
        for dy in range(-n+1, n):
            max_overlap = max(max_overlap, count_overlap(dx, dy))
    
    return max_overlap


if __name__ == "__main__":
    print("Testing Image Overlap:\n")
    
    img1 = [[1,1,0],[0,1,0],[0,1,0]]
    img2 = [[0,0,0],[0,1,1],[0,0,1]]
    
    r1 = largestOverlap(img1, img2)
    r2 = largestOverlap_slide(img1, img2)
    
    print(f"Image 1: {img1}")
    print(f"Image 2: {img2}")
    result = "✓" if r1 == 3 else "✗"
    print(f"\nTranslation={r1} Slide={r2} (exp=3) {result}")
