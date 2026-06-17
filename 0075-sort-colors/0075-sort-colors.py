class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        find = 0
        # 三路划分[0, left), [left, find], [find, right]
        while find <= r:
            # 右路 待探索区域，find指针不前进
            if nums[find] == 2:
                nums[find], nums[r] = nums[r], nums[find]
                r -= 1
            # 左路[0, left) 全是0
            elif nums[find] == 0:
                nums[find], nums[l] = nums[l], nums[find]
                l += 1
                find += 1
            # 中路[left, find) 全是1
            else:
                find += 1
        