class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp=[-1]*128
        left=0
        ans=0

        for right,c in enumerate(s):
            left=max(left,mp[ord(c)]+1)
            mp[ord(c)]=right
            ans=max(ans,right-left+1)
        return ans
        