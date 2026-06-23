class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        # 固定第一个数
        for i in range(n - 3):
            a = nums[i]
            if i > 0 and a == nums[i - 1]:
                continue
            if a + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break
            if a + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            # 固定第二个数
            for j in range(i + 1, n - 2):
                b = nums[j]
                if j > i + 1 and b == nums[j - 1]:
                    continue
                if a + b + nums[j + 1] + nums[j + 2] > target:
                    break
                if a + b + nums[-1] + nums[-2] < target:
                    continue
                # 寻找两数之和
                l, r = j + 1, n - 1
                while l < r:
                    sum = a + b + nums[l] + nums[r]
                    if sum == target:
                        ans.append([a, b, nums[l], nums[r]])
                        t = nums[l]
                        while l < r and t == nums[l]:
                            l += 1
                        k = nums[r]
                        while l < r and k == nums[r]:
                            r -= 1
                    elif sum < target:
                        l += 1
                    else:
                        r -= 1
        return ans
                