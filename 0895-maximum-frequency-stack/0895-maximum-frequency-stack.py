from collections import defaultdict
# 栈中栈
class FreqStack:

    def __init__(self):
        self.sts = []
        self.cnt = defaultdict(int)

    def push(self, val: int) -> None:
        if self.cnt[val] == len(self.sts):
            self.sts.append([val])
        else:
            self.sts[self.cnt[val]].append(val)
        self.cnt[val] += 1

    def pop(self) -> int:
        val = self.sts[-1].pop()
        # 如果栈中栈弹出最大频率元素后为空，则把空栈弹出
        if not self.sts[-1]:
            self.sts.pop()
        self.cnt[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()