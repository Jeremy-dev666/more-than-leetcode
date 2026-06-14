class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(path, index):
            if len(path) == len(digits):
                ans.append("".join(path))
                return
            
            number = digits[index]
            letters = dic[number]
            for l in letters:
                path.append(l)
                backtrack(path, index + 1)
                path.pop()

        ans = []
        backtrack([], 0)
        return ans