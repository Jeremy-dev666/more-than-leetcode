class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        # 这个边界非常重要，L可以落在整个数组的有边界外，表示右侧段个数为零
        l, r = 0, m
        while l <= r:
            div1 = (l + r) // 2
            div2 = (m + n + 1) // 2 - div1
            
            div1_left = -float('inf') if div1 == 0 else nums1[div1 - 1]
            div1_right = float('inf') if div1 == m else nums1[div1]
            div2_left = -float('inf') if div2 == 0 else nums2[div2 - 1]
            div2_right = float('inf') if div2 == n else nums2[div2]

            if div1_left <= div2_right and div2_left <= div1_right:
                if (m + n) % 2 == 1:
                    return max(div1_left, div2_left)
                else:
                    return (max(div1_left, div2_left) + min(div1_right, div2_right)) / 2.0
            elif div1_left > div2_right:
                r = div1 - 1
            else:
                l = div1 + 1
                
        return -1.0
