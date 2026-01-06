"""

                 LeetCode #468 - Validate IP Address                          
                 Topic: String | Difficulty: Medium                           
                 Company: Amazon, Microsoft                                   


PROBLEM: Determine if string is valid IPv4 or IPv6 address.

Examples:
  "172.16.254.1"  "IPv4"
  "2001:0db8:85a3:0:0:8A2E:0370:7334"  "IPv6"
  "256.256.256.256"  "Neither"
"""

#  SOLUTION 1: String Parsing (OPTIMAL)
def validIPAddress(queryIP):
    """
    Parse and validate components
    Time: O(1), Space: O(1)
    
    IPv4: 4 parts, 0-255, no leading zeros
    IPv6: 8 parts, hex (0-9, a-f), 1-4 chars
    """
    def is_ipv4(s):
        parts = s.split('.')
        if len(parts) != 4:
            return False
        
        for part in parts:
            if not part or len(part) > 3:
                return False
            if part[0] == '0' and len(part) > 1:  # Leading zero
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
        
        for part in parts:
            if not part or len(part) > 4:
                return False
            if not all(c in '0123456789abcdefABCDEF' for c in part):
                return False
        
        return True
    
    if '.' in queryIP:
        return "IPv4" if is_ipv4(queryIP) else "Neither"
    elif ':' in queryIP:
        return "IPv6" if is_ipv6(queryIP) else "Neither"
    else:
        return "Neither"


#  SOLUTION 2: Try-Except with Built-in
def validIPAddress_builtin(queryIP):
    """
    Use ipaddress module
    Time: O(1), Space: O(1)
    
    Pythonic but may not be allowed in interview.
    """
    import ipaddress
    
    try:
        return "IPv4" if type(ipaddress.ip_address(queryIP)) is ipaddress.IPv4Address else "IPv6"
    except ValueError:
        return "Neither"


if __name__ == "__main__":
    print("Testing Validate IP Address:\n")
    
    tests = [
        ("172.16.254.1", "IPv4"),
        ("2001:0db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
        ("256.256.256.256", "Neither"),
        ("2001:0db8:85a3::8A2E:0370:7334", "Neither"),
        ("192.0.0.1", "IPv4")
    ]
    
    for ip, expected in tests:
        r1 = validIPAddress(ip)
        
        print(f'"{ip}": {r1} (exp={expected}) {"" if r1 == expected else ""}')
