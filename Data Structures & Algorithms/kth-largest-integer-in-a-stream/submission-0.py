class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp=nums
        heapq.heapify(self.hp)
        self.k=k
        while self.hp and len(self.hp)>self.k:
            heapq.heappop(self.hp)

    def add(self, val: int) -> int:
        heapq.heappush(self.hp,val)
        while self.hp and len(self.hp)>self.k:
            heapq.heappop(self.hp)
        return self.hp[0]
        
