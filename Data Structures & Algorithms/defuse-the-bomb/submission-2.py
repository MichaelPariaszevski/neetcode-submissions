class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        result_arr: List[int] = [0] * len(code)

        if k == 0: 
            return result_arr
        else: 
            original_k = k
            k = k if k > 0 else -k
            curr_window = sum(code[1 : k + 1])
            result_arr[0] = curr_window
            for i in range(1, len(code)): 
                curr_window = curr_window - code[i] + code[(i + k) % len(code)]
                result_arr[i] = curr_window
            if original_k > 0: 
                return result_arr
            else: 
                return result_arr[original_k - 1:] + result_arr[:original_k - 1]

        # 1 2 3 4 5
        # 5 7 9 6 3 
        # 9 6 3 5 7

        # 2 3 1

        # 13 12 5 6