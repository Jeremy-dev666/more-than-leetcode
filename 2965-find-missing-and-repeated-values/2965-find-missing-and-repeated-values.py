from collections import defaultdict
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        dic = defaultdict(int)
        for row in grid:
            for num in row:
                dic[num] += 1
        for num in range(1, n * n + 1):
            if num not in dic:
                missing = num
            elif dic[num] == 2:
                repeat = num
        return [repeat, missing]