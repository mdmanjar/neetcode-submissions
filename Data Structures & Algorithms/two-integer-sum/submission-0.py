class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mp={}

        for i,e in enumerate(nums):
            x=target-e
            if x in mp:
                return [mp[x],i]
            mp[e]=i
        return [-1,-1]
        