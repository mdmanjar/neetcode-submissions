class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry=0
        ans=0

        for i in range(32):
            x=a&1
            y=b&1
            sm=x+y+carry

            if sm==0:
                bit=0
                carry=0
            elif sm==1:
                bit=1
                carry=0
            elif sm==2:
                bit=0
                carry=1
            else:
                bit=1
                carry=1

            ans|=bit<<i
            a>>=1
            b>>=1

        if ans>=2**31:
            ans-=2**32

        return ans

