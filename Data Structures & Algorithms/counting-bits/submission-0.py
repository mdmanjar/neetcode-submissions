arr=[]
for i in range(1001):
    c=0
    while i:
        if i&1:c+=1
        i>>=1
    arr.append(c)

class Solution:
    def countBits(self, n: int) -> List[int]:
        return arr[:n+1]
        