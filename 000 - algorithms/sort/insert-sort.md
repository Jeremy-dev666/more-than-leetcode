```java
class Solution {
    public static void insertSort(int[] arr) {
        if (arr == null || arr.length < 2) { return; }
        for (int i = 1; i < arr.length; i++) {
            // 0...i-1已经排好序，i...n未排序
            for (int j = i - 1; j >= 0 && arr[j] > arr[j + 1]; j--) {
                swap(arr, j, j + 1);
            }
        }
    }

    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
}
```