from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket = defaultdict(int)
        ans = 0
        left = right = 0
        n = len(fruits)

        while right < n:
            basket[fruits[right]] += 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1
            ans = max(ans, right - left + 1)
            
            right += 1
        
        return ans