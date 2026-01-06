"""
╔══════════════════════════════════════════════════════════════════════════════╗
║                    LeetCode #911 - Online Election                            ║
║                    Topic: Binary Search                                      ║
║                    Difficulty: Medium                                         ║
║                    Company: Amazon, Meta                                     ║
╚══════════════════════════════════════════════════════════════════════════════╝

╔══════════════════════════════════════════════════════════════════════════════╗
║                    🎯 QUESTION IN SIMPLE TERMS                               ║
╚══════════════════════════════════════════════════════════════════════════════╝

WHAT'S THE PROBLEM?
───────────────────
Votes cast at different times. Query who is leading at time t.
Ties broken by most recent vote.

EXAMPLES:
─────────
✓ Input: persons = [0,1,1,0,0,1,0], times = [0,5,10,15,20,25,30]
  Query t=3:  Leader is 0 (only vote so far)
  Query t=12: Leader is 1 (votes: 0,1,1 → 1 leads)
  Query t=25: Leader is 1 (votes: 0,1,1,0,0,1 → tied, 1 voted last)

IMAGINE THIS (CHILD-FRIENDLY):
──────────────────────────────
🏆 Sports game: Votes for players A(0) and B(1) coming in over time.
   At any moment, who's winning?
   
   Time 0: A gets vote → A leads
   Time 5: B gets vote → Tied, but B voted last → B leads
   Time 10: B gets vote → B leads (2 vs 1)

╔══════════════════════════════════════════════════════════════════════════════╗
║                    ⭐ AMAZON STAR METHOD ANSWER                              ║
╚══════════════════════════════════════════════════════════════════════════════╝

📌 SITUATION:
   Amazon polls: real-time voting, need to query leader
   at any timestamp efficiently.

📌 TASK:
   Preprocess votes, answer q queries in O(log n) each.
   Constructor: O(n), Query: O(log n).

📌 ACTION:
   1. Preprocess: track leader at each timestamp
   2. Binary search for latest vote before/at query time

📌 RESULT:
   ✓ Constructor: O(n) preprocessing
   ✓ Query: O(log n) binary search
   ✓ Fast real-time leader lookup

"""

# ═══════════════════════════════════════════════════════════════════════════
# 💡 BRUTE FORCE - Recount Each Query
# ═══════════════════════════════════════════════════════════════════════════
class TopVotedCandidate_Bruteforce:
    """
    Recount votes for every query
    
    Constructor: O(1)
    Query: O(n) - scan all votes up to time t
    """
    def __init__(self, persons, times):
        self.persons = persons
        self.times = times
    
    def q(self, t):
        # Count votes up to time t
        votes = {}
        leader = -1
        max_votes = 0
        
        for i in range(len(self.times)):
            if self.times[i] > t:
                break
            
            person = self.persons[i]
            votes[person] = votes.get(person, 0) + 1
            
            # Update leader (tie goes to most recent)
            if votes[person] >= max_votes:
                max_votes = votes[person]
                leader = person
        
        return leader


# ═══════════════════════════════════════════════════════════════════════════
# 🚀 OPTIMAL SOLUTION - Preprocessing + Binary Search
# ═══════════════════════════════════════════════════════════════════════════
class TopVotedCandidate:
    """
    Preprocess leaders, binary search for queries
    
    Example: persons = [0,1,1,0,0,1,0], times = [0,5,10,15,20,25,30]
    ────────
    Preprocessing:
    Time 0:  Person 0 votes → votes={0:1} → leader=0
    Time 5:  Person 1 votes → votes={0:1,1:1} → leader=1 (tie, 1 recent)
    Time 10: Person 1 votes → votes={0:1,1:2} → leader=1
    Time 15: Person 0 votes → votes={0:2,1:2} → leader=0 (tie, 0 recent)
    Time 20: Person 0 votes → votes={0:3,1:2} → leader=0
    Time 25: Person 1 votes → votes={0:3,1:3} → leader=1 (tie, 1 recent)
    Time 30: Person 0 votes → votes={0:4,1:3} → leader=0
    
    leaders = [0,1,1,0,0,1,0]
    
    Query t=12: Binary search times for 12 → index 2 → leader=1
    """
    def __init__(self, persons, times):
        self.times = times
        self.leaders = []
        
        votes = {}
        leader = -1
        max_votes = 0
        
        # Preprocess: calculate leader at each timestamp
        for person in persons:
            votes[person] = votes.get(person, 0) + 1
            
            # Update leader if person ties or exceeds
            if votes[person] >= max_votes:
                max_votes = votes[person]
                leader = person
            
            self.leaders.append(leader)
    
    def q(self, t):
        # Binary search for rightmost time ≤ t
        left, right = 0, len(self.times) - 1
        
        while left < right:
            mid = (left + right + 1) // 2  # Bias right for rightmost
            
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid - 1
        
        return self.leaders[left]


# ═══════════════════════════════════════════════════════════════════════════
# 📚 ALTERNATIVE - Using bisect
# ═══════════════════════════════════════════════════════════════════════════
class TopVotedCandidate_Bisect:
    """
    Same logic but using Python's bisect module
    """
    def __init__(self, persons, times):
        import bisect
        self.bisect = bisect
        self.times = times
        self.leaders = []
        
        votes = {}
        leader = -1
        max_votes = 0
        
        for person in persons:
            votes[person] = votes.get(person, 0) + 1
            if votes[person] >= max_votes:
                max_votes = votes[person]
                leader = person
            self.leaders.append(leader)
    
    def q(self, t):
        # bisect_right gives insertion point
        idx = self.bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]


# ═══════════════════════════════════════════════════════════════════════════
# 📊 COMPLEXITY COMPARISON
# ═══════════════════════════════════════════════════════════════════════════
"""
╔════════════════╦════════════════╦═══════════╦═════════════════════════╗
║   Approach     ║  Constructor   ║   Query   ║       Notes             ║
╠════════════════╬════════════════╬═══════════╬═════════════════════════╣
║ Brute Force    ║     O(1)       ║   O(n)    ║ Recount each time       ║
║ Preprocessing  ║     O(n)       ║ O(log n)  ║ Optimal solution        ║
║ With Bisect    ║     O(n)       ║ O(log n)  ║ Cleaner code            ║
╚════════════════╩════════════════╩═══════════╩═════════════════════════╝

Space: O(n) for all approaches (store leaders/persons)
"""


# ═══════════════════════════════════════════════════════════════════════════
# 🧪 TEST CASES
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    persons = [0, 1, 1, 0, 0, 1, 0]
    times = [0, 5, 10, 15, 20, 25, 30]
    queries = [3, 12, 25, 15, 24, 8]
    
    print("=" * 70)
    print("🧪 TESTING ONLINE ELECTION")
    print("=" * 70)
    
    brute = TopVotedCandidate_Bruteforce(persons, times)
    optimal = TopVotedCandidate(persons, times)
    bisect_ver = TopVotedCandidate_Bisect(persons, times)
    
    for t in queries:
        result_brute = brute.q(t)
        result_optimal = optimal.q(t)
        result_bisect = bisect_ver.q(t)
        
        print(f"\nQuery t={t}")
        print(f"Brute: {result_brute}")
        print(f"Optimal: {result_optimal}")
        print(f"Bisect: {result_bisect}")
