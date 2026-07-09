class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k

        n = len(nums)
        nums.sort(reverse=True)
        if nums[0] > target:
            return False
        used = [False] * n

        def dfs(i, subset_sum, k):
            if k == 0:
                return True
            
            if subset_sum == target:
                return dfs(0, 0, k - 1)

            for j in range(i, n):
                if used[j] or subset_sum + nums[j] > target:
                    continue

                used[j] = True
                if dfs(j + 1, subset_sum + nums[j], k):
                    return True
                used[j] = False
            return False

        return dfs(0, 0, k)