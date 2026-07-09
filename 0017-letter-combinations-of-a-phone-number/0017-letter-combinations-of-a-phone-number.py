MAPPING = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        n = len(digits)

        def dfs(path, start):
            if len(path) == n:
                ans.append(''.join(path))
                return

            number = digits[start]
            letters = MAPPING[int(number)]
            for c in letters:
                path.append(c)
                dfs(path, start+1)
                path.pop()

        dfs([], 0)
        return ans
            