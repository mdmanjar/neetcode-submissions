class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp=[0]*26
        ans=0
        left=0

        for right,c in enumerate(s):
            mp[ord(c)-65]+=1

            while (right-left+1)-max(mp)>k:
                mp[ord(s[left])-65]-=1
                left+=1

            ans=max(ans,right-left+1)

        return ans