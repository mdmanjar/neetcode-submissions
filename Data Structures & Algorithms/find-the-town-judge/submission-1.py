class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = [0]*n
        outgoing =[0]*n

        for src, dst in trust:
            outgoing[src-1] += 1
            incoming[dst-1] += 1

        for i in range(n):
            if outgoing[i] == 0 and incoming[i] == n - 1:
                return i+1

        return -1