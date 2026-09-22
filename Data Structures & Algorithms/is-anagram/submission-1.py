class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False
        mp=[0]*26
        for a,b in zip(s,t):
            mp[ord(a)-97]+=1
            mp[ord(b)-97]-=1

        for i in range(26):
            if mp[i]!=0:return False
        return True
        