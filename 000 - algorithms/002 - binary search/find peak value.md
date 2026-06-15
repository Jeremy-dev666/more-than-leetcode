```java
class Solution {
    public int findPeakElement(int[] nums) { 
        // 对于峰值的边界预设条件是数组边界左右两侧都为极小值
        int n = arr.length;
        if (n == 1) return 0;
        if (nums[0] > nums[1]) return 0;
        if (nums[n - 1] > nums[n - 2]) return n - 1;

        int left = 1, right = n - 2, ans = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid - 1] > arr[mid]) {
                right = mid - 1;
            } else if (arr[mid] > arr[mid + 1]) {
                left = mid + 1;
            } else {
                ans = mid;
                break;
            }
        }

        return ans;
    }
}
```