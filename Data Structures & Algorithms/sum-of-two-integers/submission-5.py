class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        to_sum = a & mask
        carry = b & mask

        while carry != 0: 
            new_sum = (to_sum ^ carry) & mask
            carry = ((to_sum & carry) << 1) & mask
            to_sum = new_sum

        return to_sum if to_sum <= 0x7FFFFFFF else ~(to_sum ^ mask)

        # 0100
        # 0111

        # 0011
        # 0100 1000

        # 1011
        # 0000
        