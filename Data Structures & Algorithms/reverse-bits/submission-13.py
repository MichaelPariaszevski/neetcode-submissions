class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        num = n
        counter = 0

        while num > 0: 
            set_bit = num & 1
            num = num >> 1
            result = result | (set_bit << (31 - counter))
            counter += 1

        return result