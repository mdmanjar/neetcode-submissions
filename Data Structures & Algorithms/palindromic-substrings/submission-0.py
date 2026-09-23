class Solution:
    def countSubstrings(self, s: str) -> int:
        ans=0
        def pol(i,j):
            nonlocal ans
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
                ans+=1
        for i in range(len(s)):
            pol(i,i)
            pol(i,i+1)
        return ans
            
        

        