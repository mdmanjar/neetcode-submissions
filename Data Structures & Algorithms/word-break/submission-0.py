from functools import lru_cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mp=[None]*26

        for word in wordDict:
            idx=ord(word[0])-97
            mp[idx]=(word,mp[idx])
        
        @lru_cache
        def dfs(i):
            if i==len(s):return True
            node=mp[ord(s[i])-97]

            while node:
                if s.startswith(node[0],i) and dfs(i+len(node[0])):
                    return True
                node=node[1]
            return False

        return dfs(0)
        