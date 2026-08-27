class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 0:
            return None
        if len(stones) == 1: 
            return stones[0]
        while len(stones) > 1:
            stones.sort(reverse=True)
            new_value = stones.pop(0) - stones.pop(0)
            print(new_value)
            stones.append(new_value)
        return stones[0]