class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        tails = []
        for num in nums:

            # 找到合适的插入位置
            left, right= 0, len(tails)
            while left < right:
                mid = (left + right) // 2
                if num > tails[mid]:
                    left = mid + 1
                else:
                    right = mid

            if left == len(tails):
                tails.append(num)
            else:
                tails[left] = num

        return len(tails)