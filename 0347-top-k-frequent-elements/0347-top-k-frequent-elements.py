from collections import Counter

class Solution:
    def topKFrequent(self, nums, k):

        count = Counter(nums)

        # 桶，index表示出现次数
        bucket = [[] for _ in range(len(nums)+1)]

        for num, freq in count.items():
            bucket[freq].append(num)


        res = []

        # 从高频到低频
        for freq in range(len(bucket)-1, 0, -1):

            for num in bucket[freq]:
                res.append(num)

                if len(res) == k:
                    return res