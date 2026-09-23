class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp=[-1]*26

        for i ,c in enumerate(s):
            mp[ord(c)-97]=i

        last=-1
        left=0
        ans=[]

        for i,c in enumerate(s):
            last=max(last,mp[ord(c)-97])
            if last==i:
                ans.append(i-left+1)
                left=i+1
                last=-1
        return ans
        