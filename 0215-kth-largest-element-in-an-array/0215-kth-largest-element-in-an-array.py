import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickselect(nums, k, 0, len(nums) - 1)
    
    def quickselect(self, nums, k, left, right):
        pivot_idx = self.partition(nums, left, right)
        if pivot_idx == k - 1:
            return nums[pivot_idx]
        elif pivot_idx > k - 1:
            return self.quickselect(nums, k, left, pivot_idx - 1)
        else:
            return self.quickselect(nums, k, pivot_idx + 1, right)
    
    def partition(self, nums, left, right):
        idx = random.randint(left, right)
        nums[idx], nums[right] = nums[right], nums[idx]
        pivot = nums[right]

        i, j = left, right - 1
        while True:
            while i <= j and nums[i] > pivot:
                i += 1
            while i <= j and nums[j] < pivot:
                j -= 1
            if i > j:
                break
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        nums[i], nums[right] = nums[right], nums[i]
        return i