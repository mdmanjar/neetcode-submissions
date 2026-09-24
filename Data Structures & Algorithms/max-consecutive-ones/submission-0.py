class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans=0
        one=0
        for e in nums:
            if not e:
                one=0
            else:
                one+=1
            ans=max(ans,one)
        return ans
        