class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr_count: int = 0
        result: int = 0

        for i in range(k): 
            if blocks[i] == "W": 
                curr_count += 1

        result = curr_count

        left, right = 0, k - 1

        while right + 1 < len(blocks): 
            if blocks[left] == "W": 
                curr_count -= 1
            if blocks[right + 1] == "W": 
                curr_count += 1
            result = min(result, curr_count)
            left += 1
            right += 1

        return result


        