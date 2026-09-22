class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        mp=[0]*26

        for c in s1:mp[ord(c)-97]+=1
        k=len(s1)
        count=k

        for i in range(len(s2)):

            if mp[ord(s2[i])-97]>0:
                count-=1

            mp[ord(s2[i])-97]-=1

            if count==0:
                return True

            if i+1>=k:
                if mp[ord(s2[i-k+1])-97]>=0:
                    count+=1
                mp[ord(s2[i-k+1])-97]+=1

        return False