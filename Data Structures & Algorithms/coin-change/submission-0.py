class Solution:
    def __init__(self): 
        self.memo: Dict[int, int] = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: 
            return 0
        elif amount < 0: 
            return -1
        elif amount in self.memo: 
            return self.memo[amount]

        temp_arr: List[int] = []

        for coin in coins: 
            num_coins_needed = self.coinChange(coins, amount - coin)
            if num_coins_needed >= 0: 
                temp_arr.append(num_coins_needed)

        self.memo[amount] = 1 + min(temp_arr) if len(temp_arr) > 0 else -1

        return self.memo[amount]


        
    
        