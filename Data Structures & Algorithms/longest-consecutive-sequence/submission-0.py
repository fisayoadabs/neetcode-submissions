class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sortedList = list(set(nums))
        sortedList.sort()
        result = 1
        longest = 1 
        check = True
        for i in range(len(sortedList) - 1):
            if sortedList[i] + 1 == sortedList[i+1]:
                if check:
                    result += 1
                else:
                    result = 2
                    check = True
            else:
                check = False
                longest = max(longest, result)
                result = 1
        return max(longest, result)