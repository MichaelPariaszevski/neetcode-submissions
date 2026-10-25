class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result_arr: List[int] = []
        index = len(digits) - 1
        carry: bool = True
        while carry and index >= 0: 
            if digits[index] == 9: 
                result_arr.append(0)
                index -= 1
            else: 
                carry = False

        if index < 0: 
            result_arr.append(1)
        else: 
            result_arr.append(digits[index] + 1)
            for i in range(index - 1, -1, -1): 
                result_arr.append(digits[i])

        return result_arr[::-1]


        