class Solution:
    def __init__(self): 
        self.matrix: List[List[int]]

    def rotate(self, matrix: List[List[int]]) -> None:
        self.matrix = matrix

        offset_counter = 0

        for length in range(len(matrix), -1, -2): 
            self.rotate_inner(length, offset_counter)
            offset_counter += 1

    def rotate_inner(self, length: int, offset: int): 
        if length <= 1: 
            return 

        arr: List[int] = [0] * ((length - 1) * 4)

        for i in range(length - 1):
            arr[i] = self.matrix[offset][offset + i]
            arr[length - 1 + i] = self.matrix[offset + i][offset + length - 1]
            arr[2 * (length - 1) + i] = self.matrix[offset + length - 1][offset + length - 1 - i]
            arr[3 * (length - 1) + i] = self.matrix[offset + length - 1 - i][offset]

        print(arr)

        shifted_arr = arr[-1 * (length - 1):] + arr[:-1 * (length - 1)]

        print(shifted_arr)

        for i in range(length - 1): 
            self.matrix[offset][offset + i] = shifted_arr[i]
            self.matrix[offset + i][offset + length - 1] = shifted_arr[length - 1 + i]
            self.matrix[offset + length - 1][offset + length - 1 - i] = shifted_arr[2 * (length - 1) + i]
            self.matrix[offset + length - 1 - i][offset] = shifted_arr[3 * (length - 1) + i]
