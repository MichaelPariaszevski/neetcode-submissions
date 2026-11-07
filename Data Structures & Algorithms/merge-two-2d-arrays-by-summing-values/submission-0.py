class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result_arr: List[int] = []

        nums1_ptr, nums2_ptr = 0, 0

        while nums1_ptr < len(nums1) and nums2_ptr < len(nums2): 
            if nums1[nums1_ptr][0] == nums2[nums2_ptr][0]: 
                result_arr.append([nums1[nums1_ptr][0], nums1[nums1_ptr][1] + nums2[nums2_ptr][1]])
                nums1_ptr += 1
                nums2_ptr += 1
            else: 
                if nums1[nums1_ptr][0] <= nums2[nums2_ptr][0]:
                    result_arr.append(nums1[nums1_ptr])
                    nums1_ptr += 1
                else: 
                    result_arr.append(nums2[nums2_ptr])
                    nums2_ptr += 1

        while nums1_ptr < len(nums1): 
            result_arr.append(nums1[nums1_ptr])
            nums1_ptr += 1

        while nums2_ptr < len(nums2): 
            result_arr.append(nums2[nums2_ptr])
            nums2_ptr += 1
        
        return result_arr 

