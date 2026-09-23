class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp=[]

        for u,v in points:
            heapq.heappush_max(hp,(u*u+v*v,u,v))
            if len(hp)>k:
                heapq.heappop_max(hp)
        return [[u,v] for _ ,u,v in hp]
        