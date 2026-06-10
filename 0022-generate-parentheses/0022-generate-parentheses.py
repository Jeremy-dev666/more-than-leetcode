class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(left, right, path):
            if len(path) == n * 2:
                ans.append(path)
                return
            if left < n:
                backtrack(left + 1, right, path + '(')
            if right < left:
                backtrack(left, right + 1, path + ')')

        ans = []
        backtrack(0, 0, '')
        return ans