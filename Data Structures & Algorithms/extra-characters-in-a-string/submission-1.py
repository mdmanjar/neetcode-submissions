from functools import cache
from typing import List

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root = {}

        def add(word):
            t = root
            for c in word:
                t = t.setdefault(c, {})
            t['#'] = word
            
        for word in dictionary:
            add(word)
            
        @cache
        def dfs(i):
            if i == len(s):
                return 0
            
            # Scenario 1: Skip the current character s[i] as an extra character
            ans = 1 + dfs(i + 1)
            
            # Scenario 2: Try to match words starting at index i using the Trie
            t = root
            # Track the length manually to calculate the jump correctly
            for length, c in enumerate(s[i:], start=1):
                if c not in t:
                    break
                t = t[c]
                if '#' in t:
                    # If a valid dictionary word is formed, jump past it
                    ans = min(ans, dfs(i + length))
                    
            return ans
            
        return dfs(0)

        
        