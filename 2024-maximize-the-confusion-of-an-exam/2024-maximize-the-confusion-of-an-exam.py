class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def change(to_change):
            left = right = 0
            count = 0
            ans = 0

            while right < len(answerKey):
                if answerKey[right] == to_change:
                    count += 1
                while count > k:
                    if answerKey[left] == to_change:
                        count -= 1
                    left += 1
                ans = max(ans, right - left + 1)
                right += 1
                
            return ans
        
        return max(change('F'), change('T'))