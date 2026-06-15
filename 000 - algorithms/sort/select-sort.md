```java
class solution {
    public static void selectSort(int[] arr) {
        if (arr == null || arr.length < 2) { return; }
        for (int i = 0; i < arr.length - 1; i++) {
            // minIndex是当前未排序的元素中的最小值索引
            // minIndex默认为当前索引
            int minIndex = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[minIndex]) {
                    minIndex = j;
                }
            }
            swap(arr, i, minIndex);
        }
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
```