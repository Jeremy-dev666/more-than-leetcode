import java.util.Random;

class Solution {
    Map<Integer, Integer> freq = new HashMap<>();
    Random random = new Random();
    public int[] topKFrequent(int[] nums, int k) {
        
        for (int num : nums) {
            freq.merge(num, 1, Integer::sum);
        }
        
        int size = freq.size();
        int[] unique = new int[size];
        int idx = 0;
        for (int u : freq.keySet()) {
            unique[idx++] = u;
        }
        quickSort(unique, 0, size - 1, k - 1);
        int[] ans = new int[k];
        System.arraycopy(unique, 0, ans, 0, k);
        return ans;
    }

    private void quickSort(int[] arr, int start, int end, int k) {
        if (start >= end) return;

        int p = partition(arr, start, end);
        if (p == k) return;
        else if (p < k) quickSort(arr, p + 1, end, k);
        else quickSort(arr, start, p - 1, k); 
    }

    private int partition(int[] arr, int start, int end) {
        int pivotIdx = start + random.nextInt(end - start + 1);
        int pivotFreqVal = freq.get(arr[pivotIdx]);
        swap(arr, pivotIdx, end);

        int i = start, j = end - 1;
        while (true) {
            while (i <= end - 1 && freq.get(arr[i]) > pivotFreqVal) {
                i++;
            }
            while (j >= start && freq.get(arr[j]) < pivotFreqVal) {
                j--;
            }
            if (i >= j) break;
            swap(arr, i, j);
            i++;
            j--;
        }
        swap(arr, i, end);
        return i;
    }

    private void swap(int[] arr, int left, int right) {
        int t = arr[left];
        arr[left] = arr[right];
        arr[right] = t;
    }
}