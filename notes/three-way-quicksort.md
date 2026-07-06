# 三路快速排序 (Three-Way Quicksort)

> 又称 Dutch National Flag（荷兰国旗）分区。专门为「数组中有大量重复元素」的场景设计 —— 它把数组分成 **`< pivot` / `== pivot` / `> pivot`** 三段，等于 pivot 的部分直接定位，不再参与递归。

---

## 1. 双路快排还不够好吗？

[双路快排](./two-way-quicksort.md) 已经能避免重复元素导致的退化，但它仍有浪费：

- 对数组 `[3, 3, 3, 3, 3]`，双路快排会做很多次交换，把元素来回挪动，并且仍然递归处理两个子区间。
- 本质问题：**双路快排把「等于 pivot」的元素也卷进了后续递归**，明明它们已经在最终位置了。

**三路快排的洞察**：一趟分区后，所有等于 pivot 的元素就已经排好序了，永远不必再碰。重复元素越多，省下的递归越多。极端情况 `[3,3,3,...,3]` 直接 **O(n)** 一趟搞定。

---

## 2. 核心思想：荷兰国旗问题

把数组想象成荷兰国旗的三种颜色（红 < 白 < 蓝），我们要用一趟扫描把它们分成三段。维护三个指针：

```text
[ < pivot |  == pivot  | 未处理 |  > pivot ]
 lo .. lt-1  lt ..  i-1   i .. gt  gt+1 .. hi
            ^lt          ^i        ^gt
```

- **`lt`** (less than)：`[lo, lt-1]` 都 `< pivot`。
- **`i`**：当前正在检查的元素，`[lt, i-1]` 都 `== pivot`。
- **`gt`** (greater than)：`[gt+1, hi]` 都 `> pivot`。
- **`[i, gt]`** 是尚未处理的区域。

扫描规则（`i` 从 `lt` 出发，直到 `i > gt`）：

| `arr[i]` 与 pivot 比较 | 操作 |
|----------------------|------|
| `arr[i] < pivot` | `swap(i, lt)`，`i++`，`lt++` |
| `arr[i] == pivot` | 直接 `i++`（留在中间段） |
| `arr[i] > pivot` | `swap(i, gt)`，`gt--`，**`i` 不动**（换过来的元素还没检查） |

> 易错点：`arr[i] > pivot` 时 **`i` 不能前进**，因为从 `gt` 换过来的元素是「未处理区」的，还没比较过。

---

## 3. 实现

### Java

```java
public class ThreeWayQuickSort {

    public static void sort(int[] arr) {
        if (arr == null || arr.length < 2) return;
        quickSort(arr, 0, arr.length - 1);
    }

    private static void quickSort(int[] arr, int lo, int hi) {
        if (lo >= hi) return;

        // 随机选 pivot，避免有序数组退化
        int randomIdx = lo + (int) (Math.random() * (hi - lo + 1));
        swap(arr, lo, randomIdx);
        int pivot = arr[lo];

        int lt = lo;        // arr[lo, lt-1]  < pivot
        int gt = hi;        // arr[gt+1, hi]  > pivot
        int i = lo + 1;     // arr[lt, i-1]   == pivot

        while (i <= gt) {
            if (arr[i] < pivot) {
                swap(arr, i, lt);
                i++;
                lt++;
            } else if (arr[i] > pivot) {
                swap(arr, i, gt);
                gt--;
                // i 不动！换过来的元素还没检查
            } else {
                i++;
            }
        }

        // 此时 [lt, gt] 全部 == pivot，无需递归
        quickSort(arr, lo, lt - 1);
        quickSort(arr, gt + 1, hi);
    }

    private static void swap(int[] arr, int a, int b) {
        int t = arr[a];
        arr[a] = arr[b];
        arr[b] = t;
    }
}
```

---

## 4. 单趟分区图解

数组 `[2, 5, 2, 8, 2, 1]`，pivot = 2：

```text
初始:  lt=0, i=1, gt=5      [ 2  5  2  8  2  1 ]
                              lt i           gt

i=1: arr[1]=5 > 2 → swap(1,5), gt=4, i不动
     [ 2  1  2  8  2  5 ]    lt=0 i=1 gt=4

i=1: arr[1]=1 < 2 → swap(1,0), i=2, lt=1
     [ 1  2  2  8  2  5 ]    lt=1 i=2 gt=4

i=2: arr[2]=2 == 2 → i=3
     [ 1  2  2  8  2  5 ]    lt=1 i=3 gt=4

i=3: arr[3]=8 > 2 → swap(3,4), gt=3, i不动
     [ 1  2  2  2  8  5 ]    lt=1 i=3 gt=3

i=3: arr[3]=2 == 2 → i=4   (i > gt, 停止)
     [ 1  2  2  2  8  5 ]
        └─<─┘ └==┘ └─>─┘
       lo..lt-1 lt..gt  gt+1..hi

只需递归: [1] 和 [8,5]，中间的三个 2 已就位
```

---

## 5. 复杂度

| 项目 | 复杂度 |
|------|--------|
| 平均时间 | **O(n log n)** |
| 最坏时间 | O(n²)（随机化后概率极低） |
| **全相等数组** | **O(n)** ← 三路快排的杀手锏 |
| 空间 | O(log n)（递归栈） |
| 稳定性 | **不稳定** |

---

## 6. 三种快排横向对比

| | 单路 (Lomuto) | 双路 (Hoare) | 三路 (荷兰国旗) |
|---|---|---|---|
| 指针 | 1 个 | 2 个对向 | 3 个 (`lt`/`i`/`gt`) |
| 分区段数 | 2 段 | 2 段 | **3 段** |
| 等值元素 | 全堆一侧 | 均分两侧 | **单独成段，不再递归** |
| 重复元素多时 | 退化 O(n²) | 保持 O(n log n) | **最优，可达 O(n)** |
| 实现复杂度 | 最简单 | 中等 | 稍复杂 |
| 适用场景 | 元素基本不重复 | 通用 | **重复元素多 / 键值种类少** |

**选型建议**：
- 数据**重复元素多**（如按年龄、评级、颜色等少量取值排序）→ **三路快排**。
- 通用场景 → 双路快排足够。
- 这也是 Java `Arrays.sort()` 对基本类型采用 **Dual-Pivot Quicksort** + 三路思想的原因。

---

## 7. 一句话总结

> 三路快排 = 荷兰国旗分区，一趟把数组切成 `<` / `==` / `>` 三段。
> 等于 pivot 的元素一次到位、永不再碰，重复元素越多越快。
> 代价是比双路多一个指针、逻辑稍复杂，但在键值种类少的数据上是无可争议的最优解。
