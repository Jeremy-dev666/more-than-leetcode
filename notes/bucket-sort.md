# 桶排序 (Bucket Sort)

> 一种**非比较型**排序。核心思想是「分而治之」：把元素按值域分散到若干个桶里，桶内各自排序，再按桶的顺序拼接起来。当输入数据**均匀分布**时，平均时间复杂度可达 **O(n)**。

---

## 1. 核心思想

比较型排序（快排、归并）的理论下界是 O(n log n)，因为它们只能通过两两比较获取信息。桶排序跳出了这个框架：它**利用元素的值本身**来决定大致位置，从而绕过比较下界。

三步走：

1. **散列 (Scatter)**：根据元素的值，把它放进对应的桶。值小的进前面的桶，值大的进后面的桶。
2. **排序 (Sort)**：对每个桶内部单独排序（通常用插入排序，或递归桶排序）。
3. **收集 (Gather)**：按桶的顺序，依次取出元素拼接，即得到有序序列。

```text
输入: [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]

散列到 10 个桶 (按值 * 10 分配):
  桶0: []
  桶1: [0.17, 0.12]
  桶2: [0.26, 0.21, 0.23]
  桶3: [0.39]
  桶6: [0.68]
  桶7: [0.78, 0.72]
  桶9: [0.94]

桶内排序:
  桶1: [0.12, 0.17]
  桶2: [0.21, 0.23, 0.26]
  ...

收集拼接:
  [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]
```

---

## 2. 实现

### Java（针对 [0, 1) 区间的浮点数）

```java
import java.util.*;

public class BucketSort {

    public static void sort(double[] arr) {
        if (arr == null || arr.length < 2) return;
        int n = arr.length;

        // 1. 创建 n 个桶
        List<List<Double>> buckets = new ArrayList<>(n);
        for (int i = 0; i < n; i++) buckets.add(new ArrayList<>());

        // 2. 散列：值在 [0,1)，乘以 n 得到桶下标
        for (double x : arr) {
            int idx = (int) (n * x);
            buckets.get(idx).add(x);
        }

        // 3. 桶内排序
        for (List<Double> bucket : buckets) {
            Collections.sort(bucket);   // 桶内可用插入排序
        }

        // 4. 收集
        int k = 0;
        for (List<Double> bucket : buckets) {
            for (double x : bucket) {
                arr[k++] = x;
            }
        }
    }
}
```

### Java（针对任意范围的整数）

值域不是 [0,1) 时，需要先求出 `min`/`max`，再用线性映射决定桶下标：

```java
import java.util.*;

public class BucketSortInt {

    public static void sort(int[] arr) {
        if (arr == null || arr.length < 2) return;
        int n = arr.length;

        int min = arr[0], max = arr[0];
        for (int x : arr) {
            min = Math.min(min, x);
            max = Math.max(max, x);
        }
        if (min == max) return;   // 所有元素相同，已有序

        // 桶数量可调；这里用 n 个桶
        int bucketCount = n;
        List<List<Integer>> buckets = new ArrayList<>(bucketCount);
        for (int i = 0; i < bucketCount; i++) buckets.add(new ArrayList<>());

        // 线性映射: 把 [min, max] 映射到 [0, bucketCount-1]
        for (int x : arr) {
            int idx = (int) ((long) (x - min) * (bucketCount - 1) / (max - min));
            buckets.get(idx).add(x);
        }

        for (List<Integer> bucket : buckets) {
            Collections.sort(bucket);
        }

        int k = 0;
        for (List<Integer> bucket : buckets) {
            for (int x : bucket) {
                arr[k++] = x;
            }
        }
    }
}
```

---

## 3. 复杂度分析

设有 `n` 个元素、`k` 个桶。

| 项目 | 复杂度 | 说明 |
|------|--------|------|
| 平均时间 | **O(n + k)** | 数据均匀分布时，每个桶约 n/k 个元素 |
| 最坏时间 | O(n²) | 所有元素挤进同一个桶，退化为桶内排序 |
| 空间 | O(n + k) | 桶占用的额外空间 |
| 稳定性 | **稳定**（当桶内排序稳定时） |

**为什么平均是 O(n)？**
散列和收集都是 O(n)。桶内排序的总开销，在数据均匀分布时，每个桶约 `n/k` 个元素，插入排序代价约 `(n/k)²`，共 `k` 个桶，总和约 `k · (n/k)² = n²/k`。当 `k` 取与 `n` 同阶（如 `k = n`）时，桶内排序总开销降到 O(n)，整体平均 **O(n)**。

**最坏情况**：数据极度倾斜（比如全部落入一个桶），桶排序就退化成对该桶做一次普通排序，O(n²) 或 O(n log n)。

---

## 4. 关键前提与适用场景

桶排序不是万能的，它的高效**依赖两个前提**：

1. **数据要均匀分布**：分布越均匀，每个桶元素越平均，性能越接近 O(n)。如果数据高度聚集，桶排序毫无优势。
2. **值域要已知且有界**：需要知道（或能估计）数据范围，才能设计散列函数把元素映射到桶。

适合的典型场景：
- 浮点数排在 [0, 1) 区间且分布均匀。
- 大量数据、值域范围有限（如考试分数 0–100、年龄等）。
- 作为外部排序的预处理：先用桶把数据分块，再分块处理。

不适合：
- 值域未知或极大、数据稀疏。
- 数据分布严重倾斜。

---

## 5. 桶排序 vs 计数排序 vs 基数排序

三者都是非比较型排序，常被放在一起对比：

| | 桶排序 | 计数排序 | 基数排序 |
|---|---|---|---|
| 核心 | 按值域分桶，桶内再排序 | 统计每个值出现次数 | 按每一位 (digit) 依次分配收集 |
| 桶内 | 需要再排序 | 无需（每个值一个计数） | 每轮按一位分桶 |
| 适用 | 均匀分布的连续值 | 值域小的整数 | 多位整数 / 定长字符串 |
| 时间 | O(n + k) 平均 | O(n + k) | O(d · (n + k)) |
| 关系 | 通用框架 | 桶宽=1 的特例 | 多轮桶/计数排序 |

直观理解：**计数排序是「每个桶只装一种值」的桶排序**；**基数排序是「按位反复做桶排序」**。

---

## 6. 一句话总结

> 桶排序 = 散列分桶 + 桶内排序 + 顺序收集。
> 它用空间和「数据均匀分布」的假设，换来平均 O(n) 的速度，突破了比较排序 O(n log n) 的下界。
> 一旦数据分布倾斜或值域未知，它就失去优势 —— 这正是它和快排/归并这类通用比较排序的根本区别。
