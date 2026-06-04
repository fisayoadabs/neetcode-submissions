class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff] + 1, i+1]
            else:
                hashmap[num] = i
        return []