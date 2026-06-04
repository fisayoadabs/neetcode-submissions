class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            multiplier = 1
            for j in range(len(nums)):
                if j != i:
                    multiplier *= nums[j]
            result.append(multiplier)
        return result  