"""LeetCode #406 - Queue Reconstruction by Height | Greedy | Medium"""

def reconstructQueue(people):
    """ OPTIMAL - Sort and Insert: O(n) time, O(1) space"""
    people.sort(key=lambda x: (-x[0], x[1]))
    result = []
    for person in people:
        result.insert(person[1], person)
    return result

def reconstructQueue_array(people):
    """ SOLUTION 2 - Array with Placeholders: O(n) time, O(n) space"""
    people.sort(key=lambda x: (x[0], -x[1]))
    n = len(people)
    result = [None] * n
    
    for h, k in people:
        count = 0
        for i in range(n):
            if result[i] is None:
                if count == k:
                    result[i] = [h, k]
                    break
                count += 1
    
    return result

if __name__ == "__main__":
    tests = [([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]], [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]])]
    print("Testing Queue Reconstruction:")
    for people, exp in tests:
        r1 = reconstructQueue(people[:])
        print(f"Result: {r1}")
        print(f"Expected: {exp}")
        print(f"Match: {r1 == exp}")
