class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        ans=[]
        q=deque()

        for i,e in enumerate(nums):
            
            while q and nums[q[-1]]<e:q.pop()
            q.append(i)
            if i>=k-1:

                ans.append(nums[q[0]])
                if i-q[0]+1>=k:
                    q.popleft()

        return ans
        