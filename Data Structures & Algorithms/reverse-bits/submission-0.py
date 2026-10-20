class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        num = n

        for i in range(32): 
            set_bit = num & 1
            num = num >> 1
            result = result | (set_bit << (31 - i))

        return result

        