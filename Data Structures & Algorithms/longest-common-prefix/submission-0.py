class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mn=min(strs)
        ans=[]
        for i,c in enumerate(mn):
            for word in strs:
                if c !=word[i]:return ''.join(ans)
            ans.append(c)
        return ''.join(ans)
        