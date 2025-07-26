"""
LeetCode #535 - Encode and Decode TinyURL
Topic: Hashmap
Difficulty: Medium

PROBLEM EXPLANATION:
Design a system to encode a URL to a shortened URL and decode it back.
TinyURL is a URL shortening service where you enter a URL and it returns
a short URL like http://tinyurl.com/4e9iAk.

Example:
Input: url = "https://leetcode.com/problems/design-tinyurl"
encode(url) -> "http://tinyurl.com/4e9iAk"
decode("http://tinyurl.com/4e9iAk") -> "https://leetcode.com/problems/design-tinyurl"

APPROACH:
1. Use a hashmap to store long_url -> short_url mapping
2. Use another hashmap for short_url -> long_url mapping
3. Generate unique short codes using counter or random strings
4. Base URL + unique code = shortened URL

Time Complexity: O(1) for both encode and decode
Space Complexity: O(n) where n is number of URLs
"""

class Codec:
    def __init__(self):
        """
        Initialize the codec with empty mappings
        """
        self.url_to_code = {}
        self.code_to_url = {}
        self.counter = 0
        self.base_url = "http://tinyurl.com/"
    
    def encode(self, longUrl):
        """
        Encodes a URL to a shortened URL.
        """
        # Check if URL already encoded
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]
        
        # Generate unique code using counter
        code = str(self.counter)
        self.counter += 1
        
        # Store mappings
        self.url_to_code[longUrl] = code
        self.code_to_url[code] = longUrl
        
        return self.base_url + code
    
    def decode(self, shortUrl):
        """
        Decodes a shortened URL to its original URL.
        """
        # Extract code from short URL
        code = shortUrl.replace(self.base_url, "")
        return self.code_to_url.get(code, "")


# Alternative: Using random strings
import random
import string

class Codec_Random:
    def __init__(self):
        self.url_to_code = {}
        self.code_to_url = {}
        self.base_url = "http://tinyurl.com/"
        self.code_length = 6
    
    def encode(self, longUrl):
        """Encodes using random 6-character code"""
        if longUrl in self.url_to_code:
            return self.base_url + self.url_to_code[longUrl]
        
        # Generate random code
        while True:
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=self.code_length))
            if code not in self.code_to_url:
                break
        
        self.url_to_code[longUrl] = code
        self.code_to_url[code] = longUrl
        
        return self.base_url + code
    
    def decode(self, shortUrl):
        """Decodes shortened URL"""
        code = shortUrl.replace(self.base_url, "")
        return self.code_to_url.get(code, "")


# Test cases
if __name__ == "__main__":
    codec = Codec()
    
    url1 = "https://leetcode.com/problems/design-tinyurl"
    short1 = codec.encode(url1)
    print(f"Encoded: {short1}")
    print(f"Decoded: {codec.decode(short1)}")
    print(f"Match: {codec.decode(short1) == url1}")
    
    url2 = "https://www.google.com"
    short2 = codec.encode(url2)
    print(f"\nEncoded: {short2}")
    print(f"Decoded: {codec.decode(short2)}")
    print(f"Match: {codec.decode(short2) == url2}")
