# 双路快速排序 (Two-Way Quicksort)

> 又称 Hoare 分区 / 双指针快排。它是经典快排的核心改良，专门解决「数组中存在大量重复元素时退化为 O(n²)」的问题。

---

## 1. 为什么需要双路快排？

先看朴素快排的分区（Lomuto 分区）：

```text
[ < pivot | > pivot | 未处理 ]
                       ^ i
```

它只用一个指针，把「小于 pivot」的元素往左塞，「大于等于 pivot」的留右边。

**致命缺陷**：当数组中有大量等于 pivot 的元素时（极端情况：全部相等 `[3,3,3,3,3]`），所有元素都被判为「不小于 pivot」，全部堆到一侧，分区极度不平衡 → 递归深度退化到 O(n)，整体复杂度 **O(n²)**。

双路快排的思路：**用左右两个指针向中间逼近**，把「等于 pivot」的元素均匀地分配到两侧，从而保持分区平衡。

---

## 2. 核心思想

选定一个 `pivot`，用两个指针 `i`（从左往右）和 `j`（从右往左）扫描：

- `i` 向右走，停在**第一个 ≥ pivot** 的元素。
- `j` 向左走，停在**第一个 ≤ pivot** 的元素。
- 此时 `arr[i]` 和 `arr[j]` 都「站错了队」，交换它们。
- 直到 `i` 和 `j` 相遇。

关键点：遇到「等于 pivot」的元素时，**指针停下来参与交换**。这样等值元素会被「一半扔左、一半扔右」，避免了一侧堆积。

```text
初始:   [ 5 | 3  8  4  9  1  7  6 ]   pivot = 5
        i 从左找 ≥5,  j 从右找 ≤5
        i→8,  j→1   交换 → [5, 3, 1, 4, 9, 8, 7, 6]
        i→9,  j→4   i>j 相遇,停止
最后:   把 pivot 换到分界点 → [4, 3, 1, | 5 | 9, 8, 7, 6]
```

---

## 3. 实现

### Java

```java
public class TwoWayQuickSort {

    public static void sort(int[] arr) {
        if (arr == null || arr.length < 2) return;
        quickSort(arr, 0, arr.length - 1);
    }

    private static void quickSort(int[] arr, int lo, int hi) {
        if (lo >= hi) return;
        int p = partition(arr, lo, hi);
        quickSort(arr, lo, p - 1);
        quickSort(arr, p + 1, hi);
    }

    private static int partition(int[] arr, int lo, int hi) {
        // 关键：随机选 pivot，避免有序数组退化
        int randomIdx = lo + (int) (Math.random() * (hi - lo + 1));
        swap(arr, lo, randomIdx);
        int pivot = arr[lo];

        int i = lo + 1, j = hi;
        while (true) {
            // 从左找第一个 >= pivot 的（注意必须用 < 而非 <=）
            while (i <= j && arr[i] < pivot) i++;
            // 从右找第一个 <= pivot 的（注意必须用 > 而非 >=）
            while (i <= j && arr[j] > pivot) j--;
            if (i >= j) break;
            swap(arr, i, j);
            i++;
            j--;
        }
        // j 停在最后一个 <= pivot 的位置，把 pivot 换过去
        swap(arr, lo, j);
        return j;
    }

    private static void swap(int[] arr, int a, int b) {
        int t = arr[a];
        arr[a] = arr[b];
        arr[b] = t;
    }
}
```

---

## 4. 最容易踩的坑

这是双路快排面试 / 实现中最容易写错的地方：

### 坑 1：内层循环的判断符号必须是「严格不等」

```java
while (arr[i] < pivot)  i++;   // 对：遇到等于 pivot 就停下
while (arr[i] <= pivot) i++;   // 错：跳过等于 pivot 的元素
```

如果写成 `<=`，那么所有等于 pivot 的元素都会被 `i` 跳过，等值元素又全堆到一侧 —— **双路快排就退化回了普通快排**，重复元素多时仍是 O(n²)。

> 记忆要点：**「相等就停下来交换」** 才是双路快排避免退化的精髓。让等值元素被均分到两侧。

### 坑 2：pivot 必须随机化

对**已排序**或**逆序**数组，固定取首元素作 pivot 会让每次分区只能切掉一个元素，退化为 O(n²)。随机选 pivot（或三数取中）可以把这种最坏情况的概率降到几乎为零。

### 坑 3：边界 `i <= j` 不能漏

内层 while 里加 `i <= j` 保护，防止指针越界。

---

## 5. 复杂度

| 项目 | 复杂度 |
|------|--------|
| 平均时间 | **O(n log n)** |
| 最坏时间 | O(n²)（随机化后概率极低） |
| 空间 | O(log n)（递归栈） |
| 稳定性 | **不稳定**（交换会打乱相等元素的相对顺序） |

**对比普通快排**：在「重复元素较多」的数据上，双路快排能稳定保持 O(n log n)，而 Lomuto 单路快排可能退化。

---

## 6. 一句话总结

> 双路快排 = 双指针对向逼近 + 「遇到等于 pivot 就停下交换」。
> 它把等值元素均匀分到两侧，解决了重复元素导致的分区失衡。
> 但若全部元素都相等，它仍会做大量无意义交换 —— 这正是**三路快排**要解决的问题（见 [three-way-quicksort.md](./three-way-quicksort.md)）。
