arr = [0]*1001
for i in range(1001):
    arr[i] = arr[i >> 1] + (i&1)
class Solution:
    def countBits(self, n: int) -> List[int]:
        return arr[:n+1]