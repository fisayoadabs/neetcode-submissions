class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        check = 0
        for i in nums:
            if i == 1:
                check += 1
            else:
                count = max(check, count) 
                check = 0
        count = max(check, count) 
        return count


        