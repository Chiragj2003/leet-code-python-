"""
SORTING ALGORITHMS IN PYTHON
============================
A collection of common sorting algorithms with their implementations.
Each algorithm includes time/space complexity and key characteristics.
"""


# ==============================================================================
# 1. SELECTION SORT
# Time: O(n²) all cases | Space: O(1) | NOT Stable
# Definition: Repeatedly selects the smallest element from unsorted portion and swaps it to sorted portion
# ==============================================================================
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        # Find minimum in unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Swap minimum with first unsorted element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# ==============================================================================
# 2. BUBBLE SORT
# Time: O(n) best, O(n²) avg/worst | Space: O(1) | Stable
# Definition: Repeatedly compares and swaps adjacent elements, "bubbling" largest to the end each pass
# ==============================================================================
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # Compare adjacent pairs (last i elements already sorted)
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # Early exit if no swaps occurred
        if not swapped:
            break
    return arr


# ==============================================================================
# 3. INSERTION SORT
# Time: O(n) best, O(n²) avg/worst | Space: O(1) | Stable
# Definition: Builds sorted array by picking each element and inserting it into its correct position
# ==============================================================================
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Shift elements greater than key to the right
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ==============================================================================
# 4. MERGE SORT
# Time: O(n log n) all cases | Space: O(n) | Stable
# Definition: Divide-and-conquer algorithm that splits array, recursively sorts halves, then merges them
# ==============================================================================
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    # Conquer (recursive sort)
    merge_sort(left)
    merge_sort(right)
    
    # Merge sorted halves
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    # Copy remaining elements
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
    
    return arr


# ==============================================================================
# 5. QUICK SORT
# Time: O(n log n) avg, O(n²) worst | Space: O(log n) | NOT Stable
# Definition: Picks a pivot, partitions elements around it (smaller left, larger right), recurses on partitions
# ==============================================================================
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]      # Elements < pivot
    middle = [x for x in arr if x == pivot]   # Elements = pivot
    right = [x for x in arr if x > pivot]     # Elements > pivot
    
    return quick_sort(left) + middle + quick_sort(right)


# In-place Quick Sort using Lomuto partition
def quick_sort_inplace(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_idx = _partition(arr, low, high)
        quick_sort_inplace(arr, low, pivot_idx - 1)
        quick_sort_inplace(arr, pivot_idx + 1, high)
    return arr


def _partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ==============================================================================
# 6. HEAP SORT
# Time: O(n log n) all cases | Space: O(1) | NOT Stable
# Definition: Builds a max-heap from array, then repeatedly extracts maximum to build sorted array
# ==============================================================================
def heap_sort(arr):
    n = len(arr)
    
    def heapify(size, root):
        largest = root
        left, right = 2 * root + 1, 2 * root + 2
        
        if left < size and arr[left] > arr[largest]:
            largest = left
        if right < size and arr[right] > arr[largest]:
            largest = right
        
        if largest != root:
            arr[root], arr[largest] = arr[largest], arr[root]
            heapify(size, largest)
    
    # Build max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i, 0)
    
    return arr


# ==============================================================================
# 7. COUNTING SORT
# Time: O(n + k) | Space: O(k) | Stable
# Definition: Non-comparison sort that counts occurrences of each value and reconstructs sorted array
# ==============================================================================
def counting_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    count = [0] * (max_val + 1)
    
    # Count occurrences
    for num in arr:
        count[num] += 1
    
    # Rebuild array
    idx = 0
    for val in range(len(count)):
        while count[val] > 0:
            arr[idx] = val
            idx += 1
            count[val] -= 1
    
    return arr


# ==============================================================================
# 8. RADIX SORT
# Time: O(d × (n + k)) | Space: O(n + k) | Stable
# Definition: Sorts integers by processing digits from least to most significant using counting sort
# ==============================================================================
def radix_sort(arr):
    if not arr:
        return arr
    
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        _counting_sort_by_digit(arr, exp)
        exp *= 10
    
    return arr


def _counting_sort_by_digit(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    # Count digits
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1
    
    # Cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]
    
    # Build output (reverse for stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
    
    # Copy back
    for i in range(n):
        arr[i] = output[i]


# ==============================================================================
# 9. SHELL SORT
# Time: O(n log n) to O(n²) | Space: O(1) | NOT Stable
# Definition: Improved insertion sort that compares elements far apart, gradually reducing the gap to 1
# ==============================================================================
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Gapped insertion sort
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    
    return arr


# ==============================================================================
# 10. COCKTAIL SORT (Bidirectional Bubble Sort)
# Time: O(n) best, O(n²) avg/worst | Space: O(1) | Stable
# Definition: Bubble sort variant that traverses in both directions, moving large and small elements faster
# ==============================================================================
def cocktail_sort(arr):
    n = len(arr)
    start, end = 0, n - 1
    swapped = True
    
    while swapped:
        swapped = False
        
        # Forward pass (left to right)
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        if not swapped:
            break
        
        end -= 1
        swapped = False
        
        # Backward pass (right to left)
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        start += 1
    
    return arr


# ==============================================================================
# 11. BUCKET SORT
# Time: O(n + k) avg, O(n²) worst | Space: O(n + k) | Stable
# Definition: Distributes elements into buckets, sorts each bucket individually, then concatenates results
# ==============================================================================
def bucket_sort(arr):
    if not arr:
        return arr
    
    min_val, max_val = min(arr), max(arr)
    bucket_range = (max_val - min_val) / len(arr) or 1
    
    # Create and fill buckets
    buckets = [[] for _ in range(len(arr))]
    for num in arr:
        idx = min(int((num - min_val) / bucket_range), len(arr) - 1)
        buckets[idx].append(num)
    
    # Sort buckets and concatenate
    return [num for bucket in buckets for num in sorted(bucket)]


# ==============================================================================
# 12. TIM SORT
# Time: O(n) best, O(n log n) avg/worst | Space: O(n) | Stable
# Definition: Hybrid algorithm combining insertion sort for small chunks and merge sort for combining them
# Note: Python's built-in sort() uses this algorithm
# ==============================================================================
MIN_RUN = 32


def tim_sort(arr):
    n = len(arr)
    
    # Sort small runs with insertion sort
    for start in range(0, n, MIN_RUN):
        end = min(start + MIN_RUN - 1, n - 1)
        _insertion_sort_range(arr, start, end)
    
    # Merge runs
    size = MIN_RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(n - 1, left + size - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                _merge_runs(arr, left, mid, right)
        size *= 2
    
    return arr


def _insertion_sort_range(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def _merge_runs(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]
    
    i = j = 0
    k = left
    
    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1
    
    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1
    
    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1


# ==============================================================================
# QUICK REFERENCE
# ==============================================================================
"""
Algorithm       | Best      | Average   | Worst     | Space   | Stable
----------------|-----------|-----------|-----------|---------|-------
Selection       | O(n²)     | O(n²)     | O(n²)     | O(1)    | No
Bubble          | O(n)      | O(n²)     | O(n²)     | O(1)    | Yes
Insertion       | O(n)      | O(n²)     | O(n²)     | O(1)    | Yes
Merge           | O(n logn) | O(n logn) | O(n logn) | O(n)    | Yes
Quick           | O(n logn) | O(n logn) | O(n²)     | O(logn) | No
Heap            | O(n logn) | O(n logn) | O(n logn) | O(1)    | No
Counting        | O(n+k)    | O(n+k)    | O(n+k)    | O(k)    | Yes
Radix           | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n+k)  | Yes
Shell           | O(n logn) | O(n^1.25) | O(n²)     | O(1)    | No
Cocktail        | O(n)      | O(n²)     | O(n²)     | O(1)    | Yes
Bucket          | O(n+k)    | O(n+k)    | O(n²)     | O(n+k)  | Yes
Tim             | O(n)      | O(n logn) | O(n logn) | O(n)    | Yes
"""


# ==============================================================================
# TEST ALL ALGORITHMS
# ==============================================================================
if __name__ == "__main__":
    test_cases = [
        ("Selection Sort", selection_sort, [64, 25, 12, 22, 11]),
        ("Bubble Sort", bubble_sort, [64, 34, 25, 12, 22, 11, 90]),
        ("Insertion Sort", insertion_sort, [12, 11, 13, 5, 6]),
        ("Merge Sort", merge_sort, [38, 27, 43, 3, 9, 82, 10]),
        ("Quick Sort", quick_sort, [10, 7, 8, 9, 1, 5]),
        ("Heap Sort", heap_sort, [12, 11, 13, 5, 6, 7]),
        ("Counting Sort", counting_sort, [4, 2, 2, 8, 3, 3, 1]),
        ("Radix Sort", radix_sort, [170, 45, 75, 90, 802, 24, 2, 66]),
        ("Shell Sort", shell_sort, [12, 34, 54, 2, 3]),
        ("Cocktail Sort", cocktail_sort, [5, 1, 4, 2, 8, 0, 2]),
        ("Bucket Sort", bucket_sort, [0.78, 0.17, 0.39, 0.26, 0.72]),
        ("Tim Sort", tim_sort, [5, 21, 7, 23, 19]),
    ]
    
    print("=" * 50)
    print("SORTING ALGORITHMS TEST")
    print("=" * 50)
    
    for name, func, arr in test_cases:
        original = arr.copy()
        result = func(arr.copy())
        print(f"\n{name}:")
        print(f"  Input:  {original}")
        print(f"  Output: {result}")
    
    print("\n" + "=" * 50)
    print("All tests completed!")
    print("=" * 50)
