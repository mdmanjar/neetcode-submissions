class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st=set(nums)
        ans=0

        for e in nums:
            length=0
            if e-1 not in st:
                while e in st:
                    length+=1
                    st.discard(e)
                    e+=1
            ans=max(ans,length)
        return ans
        