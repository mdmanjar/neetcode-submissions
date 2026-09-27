class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        mp={}
        for e in nums2:
            while stack and stack[-1]<e:
                mp[stack.pop()]=e
            stack.append(e)
        return [mp[e] if e in mp else -1 for e in nums1]
        