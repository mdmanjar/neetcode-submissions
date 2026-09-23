class Solution:
    def longestPalindrome(self, s: str) -> str:
        start=0
        length=0

        def pol(i,j):
            nonlocal start,length
            while i>=0 and j<len(s) and s[i]==s[j]:
                i-=1
                j+=1
            i+=1
            j-=1
            lg=j-i+1
            if length<lg:
                start=i
                length=lg
        for i in range(len(s)):
            pol(i,i)
            pol(i,i+1)
        return s[start:length+start]
            
        