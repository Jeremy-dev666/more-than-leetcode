class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for a in range(n - 2): 
            if a >= 1 and nums[a] == nums[a - 1]:
                continue
            if nums[a] + nums[n - 1] + nums[n - 2] < 0:
                continue
            if nums[a] + nums[a + 1] + nums[a + 2] > 0:
                break

            l, r = a + 1, n - 1
            while l < r:
                sum = nums[a] + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    ans.append([nums[a], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    r -= 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return ans


            