class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        mn=deque()
        mx=deque()
        ans=0
        left=0

        for right,e in enumerate(nums):

            while mn and nums[mn[-1]]>e:
                mn.pop()
            
            while mx and nums[mx[-1]]<e:
                mx.pop()
            mn.append(right)
            mx.append(right)
            while nums[mx[0]]-nums[mn[0]]>limit:
                if left==mx[0]:mx.popleft()
                if left==mn[0]:mn.popleft()
                left+=1
            ans=max(ans,right-left+1)
        return ans


        