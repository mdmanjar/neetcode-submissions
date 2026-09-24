class Solution:
    def scoreOfString(self, s: str) -> int:
        ans=0
        for i in range(1,len(s)):
            ans+=abs((ord(s[i-1])-97)-(ord(s[i])-97))
            # ans+=abs((ord(s[i+1])-97)-(ord(s[i])-97))
        return ans

        