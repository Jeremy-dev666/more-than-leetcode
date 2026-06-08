class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range (n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] + nums[-1] + nums[-2] < 0:
                continue
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break

            l = i + 1
            r = n - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1

        return ans