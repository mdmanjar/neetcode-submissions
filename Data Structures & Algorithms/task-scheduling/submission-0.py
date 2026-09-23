
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        mx = 0

        for t in tasks:
            idx = ord(t) - ord('A')
            freq[idx] += 1
            mx = max(mx, freq[idx])

        ans = (mx - 1) * (n + 1)

        for f in freq:
            if f == mx:
                ans += 1

        return max(len(tasks), ans)