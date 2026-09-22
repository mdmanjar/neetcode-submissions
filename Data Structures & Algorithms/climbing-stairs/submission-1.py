
class Solution:

    def climbStairs(self, n: int) -> int:
        one=1
        two=0

        for i in range(n+1):
            one,two=two,two+one
        return two



        