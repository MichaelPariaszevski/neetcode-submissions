class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n): 
            num = nums2[i]
            nums1[m + i] = num
            prev, curr = m + i - 1, m + i
            while prev >= 0 and nums1[curr] < nums1[prev]: 
                temp = nums1[curr]
                nums1[curr] = nums1[prev]
                nums1[prev] = temp
                prev -= 1
                curr -= 1
            

        
