class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        right = n - 2
        # 从右到左找到第一个下降元素
        while right >= 0 and nums[right] >= nums[right + 1]:
            right -= 1
        
        # 找到right右侧里比nums[right]稍大一点的元素
        if right >= 0:
            idx = n - 1
            while idx > right and nums[idx] <= nums[right]:
                idx -= 1
            
            nums[right], nums[idx] = nums[idx], nums[right]
        
        nums[right+1:] = nums[right+1:][::-1]
        

        