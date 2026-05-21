from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        self.digits = digits
        self.letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        self.ans = []
        self.backtrack(0, [])
        return self.ans

    def backtrack(self, index: int, path: List[str]) -> None:
        if len(path) == len(self.digits):
            self.ans.append("".join(path))
            return

        possible_letters = self.letters[self.digits[index]]
        for letter in possible_letters:
            path.append(letter)
            self.backtrack(index + 1, path)
            path.pop()