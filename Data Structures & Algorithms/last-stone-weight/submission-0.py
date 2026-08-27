class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return None
        if len(stones) == 1: 
            return stones[0]
        while len(stones) > 1:
            max_index = stones.index(max(stones))
            first_find = stones.pop(max_index)
            second_index = stones.index(max(stones))
            second_find = stones.pop(second_index)
            new_value = first_find - second_find
            stones.insert(max_index, new_value)
        return stones[0]