"""
LeetCode #468 - Validate IP Address
Topic: String
Difficulty: Medium

PROBLEM EXPLANATION:
Given a string, determine if it's a valid IPv4 or IPv6 address, or neither.

IPv4: Four decimal numbers (0-255) separated by dots
IPv6: Eight hexadecimal groups separated by colons

Example:
Input: queryIP = "172.16.254.1"
Output: "IPv4"

Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
Output: "IPv6"

APPROACH:
1. Check if it contains '.' or ':'
2. For IPv4: split by '.', validate 4 parts, each 0-255, no leading zeros
3. For IPv6: split by ':', validate 8 parts, each 1-4 hex digits

Time Complexity: O(n)
Space Complexity: O(1)
"""

def validIPAddress(queryIP):
    """
    Returns "IPv4", "IPv6", or "Neither"
    """
    def is_ipv4(s):
        parts = s.split('.')
        if len(parts) != 4:
            return False
        
        for part in parts:
            if not part or len(part) > 3:
                return False
            if len(part) > 1 and part[0] == '0':  # Leading zero
                return False
            if not part.isdigit():
                return False
            if int(part) > 255:
                return False
        return True
    
    def is_ipv6(s):
        parts = s.split(':')
        if len(parts) != 8:
            return False
        
        hex_chars = set('0123456789abcdefABCDEF')
        for part in parts:
            if not part or len(part) > 4:
                return False
            if not all(c in hex_chars for c in part):
                return False
        return True
    
    if '.' in queryIP:
        return "IPv4" if is_ipv4(queryIP) else "Neither"
    elif ':' in queryIP:
        return "IPv6" if is_ipv6(queryIP) else "Neither"
    else:
        return "Neither"


# Test cases
if __name__ == "__main__":
    print(f"Test 1: {validIPAddress('172.16.254.1')}")  # IPv4
    print(f"Test 2: {validIPAddress('2001:0db8:85a3:0:0:8A2E:0370:7334')}")  # IPv6
    print(f"Test 3: {validIPAddress('256.256.256.256')}")  # Neither
    print(f"Test 4: {validIPAddress('2001:0db8:85a3::8A2E:037j:7334')}")  # Neither
