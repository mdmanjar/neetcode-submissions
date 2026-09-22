class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt=Counter(nums)
        hp=[(freq,key) for key,freq in cnt.items()]
        heapq.heapify_max(hp)
        ans=[]

        while hp and k:
            _,v=heapq.heappop_max(hp)
            ans.append(v)
            k-=1
        return ans

        