from random import randint
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums

    def quicksort(self, nums, left, right):
        if left >= right:
            return

        pivot = nums[randint(left, right)]

        less = left       # < pivot 区域右边界
        cur = left        # 当前处理位置
        greater = right   # > pivot 区域左边界

        while cur <= greater:
            if nums[cur] < pivot:
                nums[less], nums[cur] = nums[cur], nums[less]
                less += 1
                cur += 1

            elif nums[cur] > pivot:
                nums[greater], nums[cur] = nums[cur], nums[greater]
                greater -= 1

            else:
                cur += 1

        self.quicksort(nums, left, less - 1)
        self.quicksort(nums, greater + 1, right)