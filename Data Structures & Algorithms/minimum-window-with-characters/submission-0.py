class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):return ''

        mp=[0]*123
        for c in t:mp[ord(c)]+=1

        start=-1
        length=len(s)+1
        count=len(t)

        left=0

        for right,c in enumerate(s):
            if mp[ord(c)]>0:
                count-=1
            mp[ord(c)]-=1

            # if count==0:
            #     x=right-left+1
            #     if length>x:
            #         length=x
            #         start=left

            while count==0:
                x=right-left+1
                if length>x:
                    length=x
                    start=left
                if mp[ord(s[left])]==0:
                    count+=1
                mp[ord(s[left])]+=1
                left+=1

        if start==-1:return ''

        return s[start:start+length]
            




        