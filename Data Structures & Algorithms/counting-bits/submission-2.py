class Solution:
    def countBits(self, n: int) -> List[int]:
        result_arr: List[int] = [0] * (n + 1)

        for i in range(1, n + 1): 
            num = i
            curr_result = 0
            while num > 0: 
                curr_result += num & 1
                num = num >> 1
            
            result_arr[i] = curr_result

        return result_arr

        