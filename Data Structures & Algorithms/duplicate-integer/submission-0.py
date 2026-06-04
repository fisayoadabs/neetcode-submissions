class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        while nums:
            num = nums[i]
            nums.pop(i)
            if num in nums:
                return True
        return False
        