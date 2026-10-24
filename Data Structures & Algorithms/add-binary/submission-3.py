class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = [0] * (max(len(a), len(b)) + 1)
        curr_ptr = 0
        while len(a) > 0 or len(b) > 0: 
            curr_a_bit = int(a[-1]) if len(a) >= 1 else 0
            curr_b_bit = int(b[-1]) if len(b) >= 1 else 0
            a = a[:-1] if len(a) >= 1 else ""
            b = b[:-1] if len(b) >= 1 else ""
            curr_sum = curr_a_bit + curr_b_bit + result[curr_ptr]
            if curr_sum <= 1: 
                result[curr_ptr] = curr_sum
            elif curr_sum == 2: 
                result[curr_ptr] = 0
                result[curr_ptr + 1] = 1
            elif curr_sum == 3: 
                result[curr_ptr] = 1
                result[curr_ptr + 1] = 1
            curr_ptr += 1

        new_result = "".join(map(str, reversed(result)))

        return new_result[1:] if new_result[0] == "0" else new_result



        