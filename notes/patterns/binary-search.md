# 二分查找 / Binary Search

> **一句话 / TL;DR**:在「有单调性/可二分判定」的搜索空间里,每次砍掉一半,O(log n) 定位目标或边界。

## 何时用 / When to use

触发信号:
- 数组**有序**,找某个值或它的插入位置
- 找「第一个满足条件」/「最后一个满足条件」的位置(下界 / 上界)
- 答案具有单调性:某阈值之后全满足、之前全不满足(二分答案)
- 局部有序/旋转数组中查找,或在「峰值」这类有方向性的结构里查找

## 核心思想 / Core idea

把问题转化为「在 `[left, right]` 区间里找分界点」。关键不是「相等就返回」,而是**想清楚找到候选后是往左还是往右继续收缩**——这决定了你拿到的是下界还是上界。用 `mid = left + (right - left) / 2` 防溢出。

## 模板代码 / Template

统一用闭区间 `[left, right]`、`while (left <= right)`,靠「记录答案 + 继续收缩方向」区分变体。

### 下界 / Lower bound(第一个 `>= target` 的位置)

```java
public int findLowerBound(int[] arr, int target) {
    int left = 0, right = arr.length - 1, ans = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] >= target) {
            ans = mid;          // 候选,继续往左找更小的下界
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return ans;
}
```

### 上界 / Upper bound(最后一个 `<= target` 的位置)

```java
public int findUpperBound(int[] arr, int target) {
    int low = 0, high = arr.length - 1, ans = -1;
    while (low <= high) {
        int mid = low + (high - low) / 2;
        if (arr[mid] <= target) {
            ans = mid;          // 候选,继续往右找更大的上界
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return ans;
}
```

### 找峰值 / Find peak(162)

```java
public int findPeakElement(int[] nums) {
    int n = nums.length;
    if (n == 1) return 0;
    if (nums[0] > nums[1]) return 0;
    if (nums[n - 1] > nums[n - 2]) return n - 1;

    int left = 1, right = n - 2, ans = -1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (nums[mid - 1] > nums[mid]) {        // 峰在左侧
            right = mid - 1;
        } else if (nums[mid] > nums[mid + 1]) { // 峰在右侧
            left = mid + 1;
        } else {                                 // 两侧都比它小,就是峰
            ans = mid;
            break;
        }
    }
    return ans;
}
```

## 变体 / Variants

| 变体 | 收缩逻辑 | 典型题 |
|---|---|---|
| 下界 lower_bound | 命中后往左 | 34, 35 |
| 上界 upper_bound | 命中后往右 | 34 |
| 找峰值 | 沿上坡方向走 | 162 |
| 旋转数组查找 | 先判断哪半有序 | 33, 153 |
| 二分答案 | 对答案空间二分 | 875, 1011 |

## 易错点 / Pitfalls

- `mid = left + (right - left) / 2` 防整型溢出,别写成 `(left + right) / 2`
- 想清楚要的是「第一个满足」还是「最后一个满足」——错了就是下界/上界搞反
- 闭区间写法务必 `while (left <= right)` 且收缩时 `mid ± 1`,否则死循环
- 找峰值前先处理 `n == 1` 和两端边界(原笔记此处用了未定义的 `arr`,已统一为 `nums`)

## 案例 / Problems

> 活表:每刷一题加一行。

| # | 题目 | 难度 | 一句话考点 | 我的解法 |
|---|---|---|---|---|
| 35 | Search Insert Position | Easy | 下界裸题 | [code](../../0035-search-insert-position/) |
| 34 | First and Last Position | Med | 下界 + 上界 | [code](../../0034-find-first-and-last-position-of-element-in-sorted-array/) |
| 33 | Search in Rotated Sorted Array | Med | 判断哪半有序 | [code](../../0033-search-in-rotated-sorted-array/) |
| 153 | Find Minimum in Rotated Sorted Array | Med | 旋转最小值 | [code](../../0153-find-minimum-in-rotated-sorted-array/) |
| 74 | Search a 2D Matrix | Med | 一维化二分 | [code](../../0074-search-a-2d-matrix/) |
| 875 | Koko Eating Bananas | Med | 二分答案 | [code](../../0875-koko-eating-bananas/) |

## 关联 / Related

- 「二分答案」常与贪心/可行性判定结合,见各案例

<!-- 标签便于检索: #pattern #binary-search -->
