class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        n1, n2 = len(num1), len(num2)
        ans = [0] * (n1 + n2)

        # 累加所有位的乘积，不立即处理进位
        for i in range(n1 - 1, -1, -1):
            d1 = ord(num1[i]) - ord('0')
            for j in range(n2 - 1, -1, -1):
                d2 = ord(num2[j]) - ord('0')
                # num1[i] 和 num2[j] 两位相乘，结果最多两位数，会落在最终结果的第 i+j 和 i+j+1 这两个位置上, i+j 表示十位数，i+j+1表示个位
                ans[i + j + 1] += d1 * d2

        # 从右到左统一处理进位
        carry = 0
        for k in range(len(ans) - 1, -1, -1):
            total = ans[k] + carry
            ans[k] = total % 10
            carry = total // 10

        # 去除前导零
        idx = 0
        # idx < len(ans) - 1 保证里ans至少有一位
        while idx < len(ans) - 1 and ans[idx] == 0:
            idx += 1
        
        return "".join(str(d) for d in ans[idx:])
        