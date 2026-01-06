"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #74 - Search a 2D Matrix                          ║
║                    Topic: Binary Search                                      ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Meta, Microsoft                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Matrix sorted row-wise and column-wise. Each row's first integer
is greater than previous row's last integer.
Search for target in O(log(m×n)).

EXAMPLES:
─────────
✓ matrix = [[1,3,5,7],
            [10,11,16,20],
            [23,30,34,60]]
  target = 3 → True

✓ target = 13 → False

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
📖 Book pages: All words sorted. If you flatten all pages into
   one long list, it's sorted. Find word fast!

🏢 Building: Apartments numbered 1,2,3... on floor 1,
   then 10,11,12... on floor 2. Find apartment #16.

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon warehouse: items in 2D grid, sorted.
   Need fast lookup.

📌 TASK:
   Search target in sorted 2D matrix.
   Time O(log(m×n)), Space O(1).

📌 ACTION:
   Binary search treating 2D as 1D:
   1. Map index to (row, col)
   2. Binary search on flattened array

📌 RESULT:
   ✓ Time: O(log(m×n)) binary search
   ✓ Space: O(1) constant
   ✓ Fast 2D search

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Linear Search
# ═══════════════════════════════════════════════════════════════════════════
def searchMatrix_bruteforce(matrix, target):
    """
    Check every element
    
    Time: O(m × n)
    Space: O(1)
    """
    for row in matrix:
        for val in row:
            if val == target:
                return True
    return False


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Binary Search (Treat as 1D)
# ═══════════════════════════════════════════════════════════════════════════
def searchMatrix(matrix, target):
    """
    Binary search treating 2D matrix as 1D array
    
    Key: Index mapping
    - 1D index i → 2D: row = i // cols, col = i % cols
    
    Example: [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    ────────
    Treat as: [1,3,5,7,10,11,16,20,23,30,34,60]
    
    left=0, right=11, mid=5
    matrix[5//4][5%4] = matrix[1][1] = 11 > 3 → search left
    
    left=0, right=4, mid=2
    matrix[0][2] = 5 > 3 → search left
    
    left=0, right=1, mid=0
    matrix[0][0] = 1 < 3 → search right
    
    left=1, right=1, mid=1
    matrix[0][1] = 3 → FOUND!
    """
    if not matrix or not matrix[0]:
        return False
    
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Map 1D index to 2D
        row = mid // cols
        col = mid % cols
        mid_val = matrix[row][col]
        
        if mid_val == target:
            return True
        elif mid_val < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Two Binary Searches
# ═══════════════════════════════════════════════════════════════════════════
def searchMatrix_twoBinary(matrix, target):
    """
    1. Binary search to find row
    2. Binary search within row
    
    Time: O(log m + log n)
    Space: O(1)
    """
    if not matrix or not matrix[0]:
        return False
    
    # Find correct row
    top, bottom = 0, len(matrix) - 1
    
    while top <= bottom:
        mid_row = (top + bottom) // 2
        if matrix[mid_row][0] <= target <= matrix[mid_row][-1]:
            # Target could be in this row
            break
        elif target < matrix[mid_row][0]:
            bottom = mid_row - 1
        else:
            top = mid_row + 1
    else:
        return False
    
    # Binary search within row
    row = (top + bottom) // 2
    left, right = 0, len(matrix[0]) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if matrix[row][mid] == target:
            return True
        elif matrix[row][mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════╦═══════════╦═════════════════════════╗
║   Approach     ║    Time    ║   Space   ║       Notes             ║
╠════════════════╬════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║   O(m×n)   ║   O(1)    ║ Check all elements      ║
║ 1D Binary      ║ O(log(m×n))║   O(1)    ║ Optimal, clean          ║
║ 2 Binary       ║O(log m+n)  ║   O(1)    ║ Row then column         ║
╚════════════════╩════════════╩═══════════╩═════════════════════════╝
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 60]
    ]
    
    test_cases = [3, 13, 1, 60, 100]
    
    print("=" * 70)
    print("🧪 TESTING SEARCH 2D MATRIX")
    print("=" * 70)
    
    for target in test_cases:
        brute = searchMatrix_bruteforce(matrix, target)
        optimal = searchMatrix(matrix, target)
        two_binary = searchMatrix_twoBinary(matrix, target)
        
        print(f"\nTarget: {target}")
        print(f"Brute: {brute}")
        print(f"1D Binary: {optimal}")
        print(f"2 Binary: {two_binary}")
