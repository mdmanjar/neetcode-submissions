class Solution:
    def lastStoneWeight(self, hp: List[int]) -> int:
        heapq.heapify_max(hp)

        while len(hp)>1:
            x=heapq.heappop_max(hp)
            y=heapq.heappop_max(hp)
            if x==y:continue
            if x>y:heapq.heappush_max(hp,x-y)
        if hp:return hp[0]
        return 0

        