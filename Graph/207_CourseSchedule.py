"""
LeetCode #207 - Course Schedule
Topic: Graph / Topological Sort
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Can you finish all courses given prerequisites?

Example:
numCourses=2, prerequisites=[[1,0]]
-> True (take course 0, then 1)

[1,0] means: must take 0 before 1

Think of it like:
Can you complete all tasks with dependencies?

WHY THIS WORKS (Simple Explanation):
Check for cycles using DFS!
If cycle exists, impossible to complete all courses.

Use 3 states:
- 0: not visited
- 1: visiting (in current path)
- 2: visited (safe)

Time: O(V + E)
Space: O(V + E)
"""

def canFinish(numCourses, prerequisites):
    """Check if can finish all courses"""
    # Build adjacency list
    graph = [[] for _ in range(numCourses)]
    for course, prereq in prerequisites:
        graph[prereq].append(course)
    
    # States: 0=not visited, 1=visiting, 2=visited
    state = [0] * numCourses
    
    def has_cycle(course):
        if state[course] == 1:  # Cycle detected!
            return True
        if state[course] == 2:  # Already checked
            return False
        
        state[course] = 1  # Mark as visiting
        
        # Check all neighbors
        for neighbor in graph[course]:
            if has_cycle(neighbor):
                return True
        
        state[course] = 2  # Mark as visited
        return False
    
    # Check each course
    for course in range(numCourses):
        if has_cycle(course):
            return False
    
    return True


# Test
if __name__ == "__main__":
    tests = [
        (2, [[1,0]], True),
        (2, [[1,0],[0,1]], False),
    ]
    
    for n, prereqs, exp in tests:
        result = canFinish(n, prereqs)
        print(f"Courses={n}, prereqs={prereqs} -> {result} (expected {exp})")
