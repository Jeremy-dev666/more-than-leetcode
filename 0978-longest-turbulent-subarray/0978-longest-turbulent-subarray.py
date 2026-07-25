class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_len = 1
        cur_len = 1
        flag = None  # None: 无方向  True:上升  False:下降

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                cur_len = 1
                flag = None

            else:
                cur_dir = arr[i - 1] < arr[i]
                if flag is None or cur_dir != flag:
                    cur_len += 1
                else:
                    cur_len = 2
                flag = cur_dir

            max_len = max(max_len, cur_len)
        
        return max_len
            
