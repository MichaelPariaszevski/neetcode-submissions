class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        counter = 1
        result: List[List[int]] = [[1]]
        curr_row: List[int] = [1]

        while counter < numRows: 
            next_row = [1]
            left, right = 0, 1
            while right < len(curr_row): 
                next_row.append(curr_row[left] + curr_row[right])
                left += 1
                right += 1

            next_row.append(1)

            counter += 1
            result.append(next_row)
            curr_row = next_row

        return result

        
        