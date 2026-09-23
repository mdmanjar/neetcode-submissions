class Solution:
    def isHappy(self, n: int) -> bool:
        def sqr_sum(n):
            ans=0
            while n:
                d=n%10
                ans+=d*d
                n//=10
            return ans
        x=sqr_sum(n)
        y=sqr_sum(x)

        while x!=y:
            x=sqr_sum(x)
            y=sqr_sum(sqr_sum(y))
        return x==1
        