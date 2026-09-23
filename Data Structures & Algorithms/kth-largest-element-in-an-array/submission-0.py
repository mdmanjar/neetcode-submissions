class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp=[]

        for e in nums:
            heapq.heappush(hp,e)
            if len(hp)>k:
                heapq.heappop(hp)
        return hp[0]
        