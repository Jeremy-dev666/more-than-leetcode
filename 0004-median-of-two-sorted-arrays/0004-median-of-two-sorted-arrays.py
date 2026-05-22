class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        
        left, right = 0, m
        while left <= right:
            # 定义两个数组的分割点
            i = left + (right - left) // 2
            j = (m + n + 1) // 2 - i

            # 通过分割点确认分割左右边界
            nums1_left_end = -math.inf if i == 0 else nums1[i - 1]
            nums1_right_start = math.inf if i == m else nums1[i]
            nums2_left_end = -math.inf if j == 0 else nums2[j - 1]
            nums2_right_start = math.inf if j == n else nums2[j]

            if nums1_left_end <= nums2_right_start \
                    and nums2_left_end <= nums1_right_start:
                left_max = max(nums1_left_end, nums2_left_end)
                right_min = min(nums1_right_start, nums2_right_start)

                if (m + n) % 2 == 1:
                    return left_max
                else:
                    return (left_max + right_min) / 2.0

            if nums1_left_end > nums2_right_start:
                right = i - 1
            else:
                left = i + 1

        return -1.0
