class Solution:
    def checkIfPrerequisite(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[bool]:
        reach=[[False]*n for _ in range(n)]

        for u,v in edges:reach[u][v]=True

        for k in range(n):
            for i in range(n):
                if reach[i][k]:
                    for j in range(n):
                        reach[i][j]|=reach[i][k] and reach[k][j]
        return [reach[i][j] for i,j in queries]
        