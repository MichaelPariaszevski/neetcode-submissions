class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap_list = []
        occurance_map = {}

        for num in nums: 
            occurance_map[num] = occurance_map.get(num, 0) + 1

        sorted_dict = dict(sorted(occurance_map.items(), key = lambda item: item[1], reverse = True))

        keys_list = list(sorted_dict.keys())

        return keys_list[:k]
