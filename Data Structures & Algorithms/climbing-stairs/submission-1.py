class Solution:
    def __init__(self): 
        self.memo: Dict[int, int] = {}

    def climbStairs(self, n: int) -> int:
        if n == 0: 
            return 1
        elif n < 0: 
            return 0
        elif n in self.memo: 
            return self.memo[n]

        one_step = self.climbStairs(n - 1)
        two_step = self.climbStairs(n - 2)

        self.memo[n - 1] = one_step
        self.memo[n - 2] = two_step

        return one_step + two_step

        