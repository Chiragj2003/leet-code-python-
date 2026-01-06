"""
LeetCode #48 - Rotate Image
Topic: Array / Matrix
Difficulty: Medium

===========================================
📌 AMAZON INTERVIEW - STAR FORMAT
===========================================

⭐ SITUATION:
    - You're building an image editing app for Amazon Photos
    - Users want to rotate their product images 90 degrees clockwise
    - The image is stored as a 2D matrix of pixel values
    - Memory is limited, so you need to do it IN-PLACE (no extra matrix)

⭐ TASK:
    - Rotate the n×n matrix 90 degrees clockwise
    - Must modify the matrix in-place (no extra space for another matrix)
    - Return nothing, just modify the input matrix

⭐ ACTION:
    Brute Force Approach: O(n²) time, O(n²) space
    - Create a new matrix
    - For each element at (i,j), place it at (j, n-1-i) in new matrix
    - Copy back to original (but this uses extra space!)
    
    Optimized Approach: O(n²) time, O(1) space
    - Step 1: Transpose the matrix (swap rows and columns)
    - Step 2: Reverse each row
    - This achieves 90° clockwise rotation!

⭐ RESULT:
    - Optimized solution uses no extra space
    - Time complexity remains O(n²) which is optimal (must touch every element)
    - Space reduced from O(n²) to O(1)

===========================================
🎯 VISUAL EXPLANATION (Like explaining to a child!)
===========================================

Imagine you have a photo with numbers:
    
    Original:           After 90° clockwise:
    [1] [2] [3]         [7] [4] [1]
    [4] [5] [6]    →    [8] [5] [2]
    [7] [8] [9]         [9] [6] [3]

HOW? Two simple steps:

Step 1: TRANSPOSE (Flip along diagonal - like folding paper diagonally)
    [1] [2] [3]         [1] [4] [7]
    [4] [5] [6]    →    [2] [5] [8]
    [7] [8] [9]         [3] [6] [9]
    
    (Row becomes Column: Row 0 [1,2,3] becomes Column 0 [1,2,3])

Step 2: REVERSE each row (Like reading backwards)
    [1] [4] [7]         [7] [4] [1]
    [2] [5] [8]    →    [8] [5] [2]
    [3] [6] [9]         [9] [6] [3]

Done! 🎉

===========================================
⏰ COMPLEXITY ANALYSIS
===========================================
BRUTE FORCE:
    Time: O(n²) - visit every element twice
    Space: O(n²) - need entire new matrix

OPTIMIZED:
    Time: O(n²) - still need to visit every element
    Space: O(1) - only swapping in place, no extra matrix!

"""

# ============================================
# 🐢 BRUTE FORCE SOLUTION
# ============================================
def rotate_brute_force(matrix):
    """
    Brute Force: Use extra space to create rotated matrix
    
    Time: O(n²) - visit each element twice
    Space: O(n²) - create new matrix of same size
    
    Simple idea:
    - Element at position (i, j) moves to position (j, n-1-i)
    - For example: top-left (0,0) goes to top-right (0, n-1)
    """
    n = len(matrix)
    
    # Step 1: Create a new matrix to store rotated result
    # Think of it like getting a blank piece of paper to copy onto
    rotated = [[0] * n for _ in range(n)]
    
    # Step 2: For each element, calculate its new position
    # In 90° clockwise rotation: (row, col) → (col, n-1-row)
    for i in range(n):
        for j in range(n):
            # Old position: (i, j)
            # New position: (j, n-1-i)
            rotated[j][n - 1 - i] = matrix[i][j]
    
    # Step 3: Copy rotated matrix back to original
    # This is necessary because we need to modify in-place
    for i in range(n):
        for j in range(n):
            matrix[i][j] = rotated[i][j]
    
    return matrix  # Optional return for testing


# ============================================
# 🚀 OPTIMIZED SOLUTION (Amazon Recommended!)
# ============================================
def rotate(matrix):
    """
    Optimized: Transpose + Reverse (In-Place!)
    
    Time: O(n²) - still need to touch every element
    Space: O(1) - NO extra matrix needed! Just swapping!
    
    Two-step process:
    1. Transpose: Flip matrix along main diagonal
    2. Reverse: Reverse each row
    
    Why this works mathematically:
    - Transpose converts (i,j) → (j,i)
    - Reverse converts (i,j) → (i, n-1-j)
    - Combined: (i,j) → (j, n-1-i) = 90° clockwise rotation!
    """
    n = len(matrix)
    
    # ============================================
    # STEP 1: TRANSPOSE the matrix
    # ============================================
    # Transpose means: swap element at (i,j) with element at (j,i)
    # We only go through UPPER triangle (j > i) to avoid double-swapping
    # 
    # Example: 
    #   [1,2,3]      [1,4,7]
    #   [4,5,6]  →   [2,5,8]
    #   [7,8,9]      [3,6,9]
    
    for i in range(n):
        # Start j from i+1 to only swap each pair once
        for j in range(i + 1, n):
            # Swap matrix[i][j] with matrix[j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # ============================================
    # STEP 2: REVERSE each row
    # ============================================
    # Example:
    #   [1,4,7]      [7,4,1]
    #   [2,5,8]  →   [8,5,2]
    #   [3,6,9]      [9,6,3]
    
    for i in range(n):
        # Python's built-in reverse - very clean!
        matrix[i].reverse()
        # Alternative: matrix[i] = matrix[i][::-1]


# ============================================
# 📝 DETAILED STEP-BY-STEP VERSION (For Learning)
# ============================================
def rotate_verbose(matrix):
    """
    Same as optimized but with detailed print statements
    Perfect for understanding what's happening at each step!
    """
    import copy
    original = copy.deepcopy(matrix)  # Save copy for comparison
    n = len(matrix)
    
    print("=" * 50)
    print("🎯 ROTATING MATRIX 90° CLOCKWISE")
    print("=" * 50)
    
    print("\n📌 ORIGINAL MATRIX:")
    for row in original:
        print(f"   {row}")
    
    # STEP 1: Transpose
    print("\n" + "=" * 50)
    print("📌 STEP 1: TRANSPOSE (Flip along diagonal)")
    print("=" * 50)
    print("Swapping (i,j) with (j,i):\n")
    
    for i in range(n):
        for j in range(i + 1, n):
            print(f"   Swap ({i},{j})={matrix[i][j]} ↔ ({j},{i})={matrix[j][i]}")
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    print("\n   After Transpose:")
    for row in matrix:
        print(f"   {row}")
    
    # STEP 2: Reverse rows
    print("\n" + "=" * 50)
    print("📌 STEP 2: REVERSE each row")
    print("=" * 50)
    
    for i in range(n):
        old_row = matrix[i].copy()
        matrix[i].reverse()
        print(f"   Row {i}: {old_row} → {matrix[i]}")
    
    print("\n" + "=" * 50)
    print("✅ FINAL ROTATED MATRIX:")
    print("=" * 50)
    for row in matrix:
        print(f"   {row}")
    
    return matrix


# ============================================
# 🔄 ALTERNATIVE: Layer by Layer Rotation
# ============================================
def rotate_layer_by_layer(matrix):
    """
    Alternative approach: Rotate layer by layer from outside to inside
    
    Think of it like an onion - rotate outer layer, then inner layer
    
    Time: O(n²)
    Space: O(1)
    
    This method rotates 4 elements at a time in a cycle:
    top → right → bottom → left → top
    """
    n = len(matrix)
    
    # Process each layer (from outer to inner)
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer
        
        for i in range(first, last):
            offset = i - first
            
            # Save top element
            top = matrix[first][i]
            
            # Move left → top
            matrix[first][i] = matrix[last - offset][first]
            
            # Move bottom → left
            matrix[last - offset][first] = matrix[last][last - offset]
            
            # Move right → bottom
            matrix[last][last - offset] = matrix[i][last]
            
            # Move top → right
            matrix[i][last] = top


# ============================================
# 🧪 TEST CASES
# ============================================
if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("🧪 TESTING ROTATE IMAGE SOLUTIONS")
    print("=" * 60)
    
    # Test Case 1: 3x3 Matrix
    print("\n📌 TEST 1: 3x3 Matrix")
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"   Input:    {matrix1}")
    rotate(matrix1)
    print(f"   Output:   {matrix1}")
    print(f"   Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]")
    
    # Test Case 2: 4x4 Matrix
    print("\n📌 TEST 2: 4x4 Matrix")
    matrix2 = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    print(f"   Input:    {matrix2}")
    rotate(matrix2)
    print(f"   Output:   {matrix2}")
    
    # Test Case 3: 2x2 Matrix
    print("\n📌 TEST 3: 2x2 Matrix")
    matrix3 = [[1, 2], [3, 4]]
    print(f"   Input:    {matrix3}")
    rotate(matrix3)
    print(f"   Output:   {matrix3}")
    print(f"   Expected: [[3, 1], [4, 2]]")
    
    # Test Case 4: 1x1 Matrix
    print("\n📌 TEST 4: 1x1 Matrix (Edge Case)")
    matrix4 = [[1]]
    print(f"   Input:    {matrix4}")
    rotate(matrix4)
    print(f"   Output:   {matrix4}")
    print(f"   Expected: [[1]]")
    
    # Verbose Example
    print("\n" + "=" * 60)
    print("📝 DETAILED WALKTHROUGH")
    print("=" * 60)
    matrix_demo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_verbose(matrix_demo)
    
    # Compare Brute Force vs Optimized
    print("\n" + "=" * 60)
    print("🐢 vs 🚀 BRUTE FORCE vs OPTIMIZED")
    print("=" * 60)
    
    matrix_bf = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_opt = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    rotate_brute_force(matrix_bf)
    rotate(matrix_opt)
    
    print(f"\n   Brute Force Result: {matrix_bf}")
    print(f"   Optimized Result:   {matrix_opt}")
    print(f"   Both match: {matrix_bf == matrix_opt} ✓")
