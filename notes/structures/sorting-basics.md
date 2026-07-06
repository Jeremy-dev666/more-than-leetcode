# 基础排序 / Elementary Sorts

> **一句话 / TL;DR**:冒泡、插入、选择三种 O(n²) 基础排序,理解它们是理解排序稳定性、最优情况差异的基础。

## 对比 / Comparison

| 算法 | 最好 | 最坏 | 平均 | 空间 | 稳定 | 特点 |
|---|---|---|---|---|---|---|
| 冒泡 Bubble | O(n)* | O(n²) | O(n²) | O(1) | 稳定 | 相邻交换;*加提前退出才有 O(n) |
| 插入 Insert | O(n) | O(n²) | O(n²) | O(1) | 稳定 | 近乎有序时极快 |
| 选择 Select | O(n²) | O(n²) | O(n²) | O(1) | 不稳定 | 交换次数最少(O(n)) |

## 代码 / Code

### 冒泡 / Bubble sort

```java
public static void bubbleSort(int[] arr) {
    if (arr == null || arr.length < 2) return;
    for (int end = arr.length - 1; end > 0; end--) {
        for (int i = 0; i < end; i++) {
            if (arr[i] > arr[i + 1]) {
                swap(arr, i, i + 1);
            }
        }
    }
}
```

### 插入 / Insertion sort

```java
public static void insertSort(int[] arr) {
    if (arr == null || arr.length < 2) return;
    for (int i = 1; i < arr.length; i++) {
        // 0..i-1 已排好序,i..n-1 未排序
        for (int j = i - 1; j >= 0 && arr[j] > arr[j + 1]; j--) {
            swap(arr, j, j + 1);
        }
    }
}
```

### 选择 / Selection sort

```java
public static void selectSort(int[] arr) {
    if (arr == null || arr.length < 2) return;
    for (int i = 0; i < arr.length - 1; i++) {
        int minIndex = i;   // 未排序部分的最小值索引
        for (int j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        swap(arr, i, minIndex);
    }
}

private static void swap(int[] arr, int i, int j) {   // 原 bubble 笔记此处缺 int[] 类型,已修正
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}
```

## 易错点 / Pitfalls

- 冒泡想拿到 O(n) 最好情况,需加「本轮无交换就提前退出」的 flag
- 选择排序**不稳定**(远距离交换会打乱相等元素的相对顺序)
- 插入排序对「近乎有序」的数据特别快,实战中小数组常用它

## 关联 / Related

- 进阶排序(快排/归并/堆排)另起笔记
- 插入排序的链表版见 [code](../../0147-insertion-sort-list/)

<!-- 标签便于检索: #structure #sorting -->
