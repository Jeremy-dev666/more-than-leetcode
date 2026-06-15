```java
class Solution {
    public int findLowerBound(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        int ans = -1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] >= target) {
                // 找到了第一个下界，记录答案，并继续往左找更小的下界
                ans = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return ans;
    }
}
```