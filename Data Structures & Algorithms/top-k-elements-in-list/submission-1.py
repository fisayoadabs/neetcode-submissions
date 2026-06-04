class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        result = []
        for i in set(nums):
            hashmap[i] = nums.count(i)
        sortDict = sorted(hashmap.items(), reverse=True, key=lambda kv: (kv[1], kv[0]))
        for i in sortDict[:k]:
            result.append(i[0])
        return result