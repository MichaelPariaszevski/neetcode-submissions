class Solution:
    def __init__(self): 
        self.result: List[int]
        self.index: int = 0
        self.result_arr_len: int

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        starting_hor_len = len(matrix[0])
        starting_ver_len = len(matrix)

        result_arr_len = starting_hor_len * starting_ver_len
        self.result_arr_len = result_arr_len
        self.result = [0] * result_arr_len

        curr_hor_len = starting_hor_len
        curr_ver_len = starting_ver_len
        curr_offset = 0

        while curr_hor_len > 0 and curr_ver_len > 0: 
            self.spiralOrderInner(matrix, curr_offset, curr_ver_len, curr_hor_len)
            curr_offset += 1
            curr_ver_len -= 2
            curr_hor_len -= 2

        if self.index == result_arr_len - 1: 
            self.result[self.index] = matrix[starting_ver_len // 2][starting_hor_len // 2]

        return self.result

    def spiralOrderInner(self, matrix: List[List[int]], offset: int, ver_len: int, hor_len: int): 
        for i in range(hor_len - 1): 
            self.result[self.index] = matrix[offset][offset + i]
            self.index += 1
            if self.index >= self.result_arr_len: 
                return

        for i in range(ver_len - 1): 
            self.result[self.index] = matrix[offset + i][offset + hor_len - 1]
            self.index += 1 
            if self.index >= self.result_arr_len: 
                return

        for i in range(hor_len - 1): 
            self.result[self.index] = matrix[offset + ver_len - 1][offset + hor_len - 1 - i]
            self.index += 1
            if self.index >= self.result_arr_len: 
                return
        
        for i in range(ver_len - 1): 
            self.result[self.index] = matrix[offset + ver_len - 1 - i][offset]
            self.index += 1
            if self.index >= self.result_arr_len: 
                return

        # 1 2 3 4 
        # 5 6 7 8 
        # 1 2 3 4 
        