"""
LeetCode #743 - Network Delay Time
Topic: Graph / Dijkstra
Difficulty: Medium

PROBLEM EXPLANATION (Easy Terms):
Signal sent from node k, travels through edges.
Find time for all nodes to receive signal.

Example:
times = [[2,1,1],[2,3,1],[3,4,1]], n=4, k=2
-> 2 (max time to reach any node)

Think of it like:
Broadcasting message through network!

WHY THIS WORKS:
Dijkstra's shortest path algorithm!
Find shortest time to each node.

Time: O(E log V)
Space: O(V + E)
"""

import heapq
from collections import defaultdict

def networkDelayTime(times, n, k):
    """Find network delay time"""
    # Build graph
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))
    
    # Dijkstra
    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0
    heap = [(0, k)]
    
    while heap:
        time, node = heapq.heappop(heap)
        
        if time > dist[node]:
            continue
        
        for neighbor, weight in graph[node]:
            new_time = time + weight
            if new_time < dist[neighbor]:
                dist[neighbor] = new_time
                heapq.heappush(heap, (new_time, neighbor))
    
    max_time = max(dist.values())
    return max_time if max_time != float('inf') else -1


# Test
if __name__ == "__main__":
    times = [[2,1,1],[2,3,1],[3,4,1]]
    result = networkDelayTime(times, 4, 2)
    print(f"Network delay: {result}")
