class Solution:
    def isHappy(self, n: int) -> bool:
        visited_set: Set[int] = set()

        while n != 1: 
            curr_val: int = 0
            
            while n > 0: 
                last_digit = n % 10
                n = n // 10
                curr_val += last_digit ** 2

            if curr_val in visited_set: 
                return False

            visited_set.add(curr_val)
            n = curr_val

        return True
        