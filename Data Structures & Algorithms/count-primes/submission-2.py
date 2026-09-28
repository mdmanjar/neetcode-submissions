limit = 5000001

prime = [True] * limit
prime[0] = prime[1] = False

for i in range(2, int(limit ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, limit, i):
            prime[j] = False

ans = [0] * limit

for i in range(1, limit):
    ans[i] = ans[i - 1] + prime[i]


class Solution:
    def countPrimes(self, n: int) -> int:
        return ans[n - 1] if n > 0 else 0
        