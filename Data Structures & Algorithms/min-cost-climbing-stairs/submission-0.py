class Solution:
    def __init__(self): 
        self.memo: Dict[int, int] = {}
        self.cost: List[int]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.cost = cost

        return min(self.iterate_up(0), self.iterate_up(1))

    def iterate_up(self, index: int): 
        if index >= len(self.cost): 
            return 0 
        elif index in self.memo: 
            return self.memo[index]

        curr_cost = self.cost[index] + min(self.iterate_up(index + 1), self.iterate_up(index + 2))

        self.memo[index] = curr_cost
    
        return curr_cost
        
        