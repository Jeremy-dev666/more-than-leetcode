class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:

        # 提前剪枝 总和能否被4整除
        n = len(matchsticks)
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False
        side = perimeter // 4

        # 预开一个路径数组保存选择
        matchsticks.sort(reverse=True)
        sides = [0 for _ in range(4)]

        def dfs(index):
            if index == n:
                return sides[0] == sides[1] == sides[2] == side
            
            # 把火柴棒枚举放到四个桶里
            for i in range(4):
                if sides[i] + matchsticks[index] <= side:
                    sides[i] += matchsticks[index]
                    if dfs(index+1):
                        return True
                    sides[i] -= matchsticks[index]
            return False

        return dfs(0)

