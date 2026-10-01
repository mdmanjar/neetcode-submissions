class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        sm = sum(nums)
        if sm % k:
            return False

        x = sm // k
        nums.sort(reverse=True)

        if nums[0] > x:
            return False

        used = [False] * len(nums)

        def dfs(target, k):
            if k == 1:
                return True

            if target == x:
                return dfs(0, k - 1)

            prev = -1

            for i, e in enumerate(nums):
                if used[i] or e == prev:
                    continue

                if target + e > x:
                    continue

                used[i] = True

                if dfs(target + e, k):
                    return True

                used[i] = False
                prev = e

                # If this element starts an empty subset and fails,
                # no other element can make that subset work.
                if target == 0:
                    break

            return False

        return dfs(0, k)