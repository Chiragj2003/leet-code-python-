"""
LeetCode #811 - Subdomain Visit Count
Topic: Hashmap
Difficulty: Medium

PROBLEM EXPLANATION:
Given an array of count-paired domains, return a list of count-paired domains
showing the number of visits each subdomain received.

Example:
Input: cpdomains = ["9001 discuss.leetcode.com"]
Output: ["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]

Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: ["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org",
         "5 org","1 intel.mail.com","951 com"]

APPROACH:
1. Use a hashmap to count visits for each domain and subdomain
2. For each count-paired domain, split into count and domain
3. Split domain and add count to all subdomains
4. Format and return results

Example: "900 google.mail.com" contributes to:
- google.mail.com: 900
- mail.com: 900
- com: 900

Time Complexity: O(n * m) where m is avg domain parts
Space Complexity: O(n * m)
"""

def subdomainVisits(cpdomains):
    """
    Returns list of count-paired domains with total visits
    """
    domain_count = {}
    
    for cpdomain in cpdomains:
        # Split count and domain
        count, domain = cpdomain.split()
        count = int(count)
        
        # Split domain into parts
        parts = domain.split('.')
        
        # Add count to all subdomains
        for i in range(len(parts)):
            subdomain = '.'.join(parts[i:])
            domain_count[subdomain] = domain_count.get(subdomain, 0) + count
    
    # Format results
    result = []
    for domain, count in domain_count.items():
        result.append(f"{count} {domain}")
    
    return result


# Test cases
if __name__ == "__main__":
    test1 = ["9001 discuss.leetcode.com"]
    print(f"Test 1: {subdomainVisits(test1)}")
    # Expected: ["9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"]
    
    test2 = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(f"Test 2: {subdomainVisits(test2)}")
    # Expected: ["901 mail.com", "50 yahoo.com", "900 google.mail.com", 
    #            "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"]
    
    test3 = ["100 a.b.c.d"]
    print(f"Test 3: {subdomainVisits(test3)}")
    # Expected: ["100 a.b.c.d", "100 b.c.d", "100 c.d", "100 d"]
