class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        self.quicksort(nums, 0, n - 1)
        return nums[n - k]

    def quicksort(self, nums, lo, hi):
        # 当前区间只有一个元素或者为空，不需要排序
        if lo >= hi:
            return

        # 随机选择 pivot，避免最坏情况 O(n^2)
        rand_idx = random.randint(lo, hi)

        # 必须把 pivot 放到当前区间左边 nums[lo]
        nums[lo], nums[rand_idx] = nums[rand_idx], nums[lo]

        pivot = nums[lo]


        # 三路快排：
        #
        # nums[lo : lt)     < pivot
        # nums[lt : i)      = pivot
        # nums[i : gt + 1)  未处理区域
        # nums[gt + 1 : hi+1) > pivot
        #
        # 注意：
        # 这里的区间都是左闭右开思想


        lt = lo        # < pivot 区域的右边界
        gt = hi        # > pivot 区域的左边界
        i = lo + 1     # 当前扫描位置
                    # nums[lo] 已经是 pivot，所以从 lo+1 开始


        while i <= gt:

            if nums[i] < pivot:
                # 当前元素应该放到 < pivot 区域

                nums[i], nums[lt] = nums[lt], nums[i]

                # 扩大 < pivot 区域
                lt += 1

                # 当前元素已经归位，继续扫描
                i += 1


            elif nums[i] > pivot:
                # 当前元素应该放到 > pivot 区域

                nums[i], nums[gt] = nums[gt], nums[i]

                # 缩小 > pivot 区域
                gt -= 1

                # i 不增加，因为换过来的 nums[i]
                # 还没有判断，可能仍然需要处理


            else:
                # nums[i] == pivot
                # 属于中间区域

                i += 1



        # 循环结束：
        #
        # nums[lo : lt]     < pivot
        # nums[lt : gt+1]   = pivot
        # nums[gt+1 : hi+1] > pivot

        # 中间这一段已经排好，=pivot, 不需要递归


        # 只需要继续排序左边 < pivot 的部分
        self.quicksort(nums, lo, lt - 1)

        # 只需要继续排序右边 > pivot 的部分
        self.quicksort(nums, gt + 1, hi)