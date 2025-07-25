"""
LeetCode #911 - Online Election
Topic: Binary Search
Difficulty: Medium

PROBLEM EXPLANATION:
In an election, persons[i] receives a vote at time times[i].
Implement TopVotedCandidate class:
- Constructor: Initialize with persons and times arrays
- q(t): Return person who was leading at time t (most votes up to time t)
  If there's a tie, the most recent vote wins.

Example:
Input: persons = [0,1,1,0,0,1,0], times = [0,5,10,15,20,25,30]
q(3) -> 0   (at time 3, person 0 is leading with 1 vote)
q(12) -> 1  (at time 12, person 1 is leading with 2 votes)
q(25) -> 1  (at time 25, it's a tie 3-3, but person 1 voted most recently)

APPROACH:
1. Pre-process: Calculate leader at each voting time
2. Store leader at each time in an array
3. For query q(t), use binary search to find the rightmost time <= t
4. Return the leader at that time

Time Complexity: O(n) for init, O(log n) per query
Space Complexity: O(n)
"""

import bisect

class TopVotedCandidate:
    def __init__(self, persons, times):
        """
        Initialize with persons and times arrays
        """
        self.times = times
        self.leaders = []
        
        vote_count = {}
        leader = -1
        max_votes = 0
        
        # Calculate leader at each time point
        for person in persons:
            # Update vote count
            vote_count[person] = vote_count.get(person, 0) + 1
            
            # Update leader if this person has most votes
            # or ties with current leader (most recent wins)
            if vote_count[person] >= max_votes:
                max_votes = vote_count[person]
                leader = person
            
            self.leaders.append(leader)
    
    def q(self, t):
        """
        Return the person leading at time t
        """
        # Find rightmost time <= t using binary search
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]


# Test cases
if __name__ == "__main__":
    persons = [0, 1, 1, 0, 0, 1, 0]
    times = [0, 5, 10, 15, 20, 25, 30]
    
    obj = TopVotedCandidate(persons, times)
    
    print(f"q(3): {obj.q(3)}")    # Expected: 0
    print(f"q(12): {obj.q(12)}")  # Expected: 1
    print(f"q(25): {obj.q(25)}")  # Expected: 1
    print(f"q(15): {obj.q(15)}")  # Expected: 0
    print(f"q(24): {obj.q(24)}")  # Expected: 0
    print(f"q(8): {obj.q(8)}")    # Expected: 1
    
    # Explanation of results:
    # Time 0: [0] - leader: 0
    # Time 5: [0,1] - leader: 0 (tie, but 0 was leading)
    # Time 10: [0,1,1] - leader: 1
    # Time 15: [0,0,1,1] - leader: 1 (tie, but 1 most recent)
    # Wait, let me recalculate...
    # Actually at time 15: votes are {0:2, 1:2}, leader changes to 0
    # At time 25: votes are {0:3, 1:3}, leader stays 1 (most recent)
