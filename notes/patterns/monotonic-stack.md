# 单调栈 / Monotonic Stack

> **一句话 / TL;DR**:维护一个单调(递增或递减)的栈,在 O(n) 内为每个元素求出「下一个/上一个更大或更小的元素」。

## 何时用 / When to use

触发信号(看到这些就该想到本模式):
- 求每个元素**左/右第一个比它大/小**的元素
- 「下一个更大元素」(Next Greater Element)
- 柱状图最大矩形、接雨水这类「向两边扩展到第一个矮的」问题
- 暴力是 O(n²) 的两层循环找邻近极值

## 核心思想 / Core idea

栈里只保留「还没找到答案的候选元素」。当新元素到来,它会把栈里所有「打破单调性」的元素弹出——而**弹出的那一刻,新元素恰好就是被弹元素要找的答案**(下一个更大/更小)。因为每个元素最多进栈一次、出栈一次,总复杂度 O(n)。栈内存**下标**而非值,这样既能取值也能算距离。

## 模板代码 / Template

```python
def next_greater(nums):
    n = len(nums)
    stack = []          # 存下标,栈内对应的值单调递减
    res = [-1] * n      # res[i] = nums 中 i 右侧第一个更大元素的下标
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            idx = stack.pop()
            res[idx] = i        # x 是 idx 的「下一个更大元素」
        stack.append(i)
    return res
```

## 变体 / Variants

| 变体 | 栈的单调性 | 典型题 |
|---|---|---|
| 下一个更大 | 递减栈 | 496, 739 |
| 下一个更小 | 递增栈 | — |
| 柱状图最大矩形 | 递增栈 + 哨兵 | 84, 85 |
| 接雨水(按层) | 递减栈 | 42 |

## 易错点 / Pitfalls

- 存**下标**而非值,否则拿不到位置/距离信息
- `<` 还是 `<=` 决定相等元素如何处理(影响 84 这类题的正确性)
- 循环结束后栈里可能有残留元素,需用**哨兵**(在数组首尾补 0/极值)统一处理
- 想清楚要的是「严格更大」还是「大于等于」

## 案例 / Problems

> 活表:每刷一题加一行。

| # | 题目 | 难度 | 一句话考点 | 我的解法 |
|---|---|---|---|---|
| 84 | Largest Rectangle in Histogram | Hard | 递增栈 + 哨兵 | [code](../../0084-largest-rectangle-in-histogram/) |
| 42 | Trapping Rain Water | Hard | 递减栈按层接水 | [code](../../0042-trapping-rain-water/) |
| 735 | Asteroid Collision | Med | 栈模拟碰撞 | [code](../../0735-asteroid-collision/) |

## 关联 / Related

- 对比 [滑动窗口](./sliding-window.md):单调队列(239)是单调栈思想在窗口上的延伸
- 进阶 [接雨水深挖](../deep-dives/0042-trapping-rain-water.md)

<!-- 标签便于检索: #pattern #stack -->
