import sys
sys.setrecursionlimit(1000000)

class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dr = (-1, 0, 1, 0)
        dc = (0, 1, 0, -1)

        def dfs(i, j):
            if (i, j) == (m - 1, n - 1):
                return True

            visit[i][j] = True

            for k in range(4):
                u, v = i + dr[k], j + dc[k]

                if not (0 <= u < m and 0 <= v < n and not visit[u][v]):
                    continue

                diff = abs(grid[i][j] - grid[u][v])

                if diff <= limit and dfs(u, v):
                    return True

            return False

        left = 0
        right = max(max(row) for row in grid) - min(min(row) for row in grid)

        while left < right:
            limit = left + (right - left) // 2
            visit = [[False] * n for _ in range(m)]

            if dfs(0, 0):
                right = limit
            else:
                left = limit + 1

        return left