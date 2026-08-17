class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = sorted(nums)[len(nums) - k:] if len(nums) - k >= 0 else sorted(nums)
        self.k = k
        

    def add(self, val: int) -> int:
        if len(self.min_heap) == 0: 
            self.min_heap.append(val)
            return self.min_heap[0]
        elif val <= self.min_heap[0]: 
            return self.min_heap[0]
        elif len(self.min_heap) < self.k:
             self.min_heap = [val] + self.min_heap
        else: 
            self.min_heap[0] = val 

        i = 0

        while True: 
            left_index = (2 * i) + 1
            right_index = left_index + 1
            left = self.min_heap[left_index] if left_index < self.k else None
            right = self.min_heap[right_index] if right_index < self.k else None
            if left is None and right is None: 
                break

            if left is not None and right is not None:
                (lowest_child, lowest_child_index) = (left, left_index) if left <= right else (right, right_index)
                if lowest_child < self.min_heap[i]: 
                    temp = self.min_heap[i]
                    self.min_heap[i] = self.min_heap[lowest_child_index]
                    self.min_heap[lowest_child_index] = temp
                    i = lowest_child_index
                    continue
                else: 
                    break
            elif left is not None and right is None: 
                if left < self.min_heap[i]: 
                    temp = self.min_heap[i]
                    self.min_heap[i] = self.min_heap[left_index]
                    self.min_heap[left_index] = temp
                    i = left_index
                    continue
                else: 
                    break
            elif left is None and right is not None: 
                if right < self.min_heap[i]: 
                    temp = self.min_heap[i]
                    self.min_heap[i] = self.min_heap[right_index]
                    self.min_heap[right_index] = temp
                    i = right_index
                    continue
                else: 
                    break

        return self.min_heap[0]

        
