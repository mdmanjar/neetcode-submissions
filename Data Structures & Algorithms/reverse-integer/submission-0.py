class Solution:
    def reverse(self, x: int) -> int:
        sign=1
        if x<0:sign=-1

        inf=2**31-1

        x=abs(x)
        rev=0

        while x:
            rev=rev*10+x%10
            x//=10
            if rev>=inf:
                return 0
        return sign*rev
        