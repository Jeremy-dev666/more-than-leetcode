class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = []
        mp = {}
        
        for num in nums2:
            while st and num > st[-1]:
                mp[st.pop()] = num
            st.append(num)

        return [mp.get(i, -1) for i in nums1]
