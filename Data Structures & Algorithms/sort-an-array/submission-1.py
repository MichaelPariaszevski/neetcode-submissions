class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums
        
    def mergeSort(self, arr: List[int], left: int, right: int) -> None: 
        if left < right: 
            mid = (left + right) // 2

            self.mergeSort(arr, left, mid)
            self.mergeSort(arr, mid + 1, right)
            self.merge(arr, left, mid, right)

    def merge(self, arr: List[int], left: int, mid: int, right: int) -> None: 
        len_left = mid - left + 1
        len_right = right - mid

        temp_left_arr = [0] * len_left
        temp_right_arr = [0] * len_right
        
        for i in range(len_left): 
            temp_left_arr[i] = arr[left + i]

        for i in range(len_right): 
            temp_right_arr[i] = arr[mid + 1 + i]

        left_index, right_index = 0, 0
        write_index = left

        while left_index < len_left and right_index < len_right: 
            if temp_left_arr[left_index] <= temp_right_arr[right_index]: 
                arr[write_index] = temp_left_arr[left_index]
                left_index += 1
            else: 
                arr[write_index] = temp_right_arr[right_index]
                right_index += 1
            write_index += 1

        while left_index < len_left: 
            arr[write_index] = temp_left_arr[left_index]
            left_index += 1
            write_index += 1

        while right_index < len_right: 
            arr[write_index] = temp_right_arr[right_index]
            right_index += 1
            write_index += 1
                
