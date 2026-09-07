class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 3:
            check = nums[0] + nums[1] + nums[2]
            if check == 0:
                return [nums]
            else:
                return []
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i+1
            right = len(nums) - 1
            while left < right:
                check = nums[i] + nums[left] + nums[right]
                if check == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < len(nums)-1 and nums[left] == nums[left + 1]:
                        left += 1
                    while right > 0 and nums[right] == nums[right - 1]:
                        right -= 1
                elif check > 0:
                    right-=1
                    continue
                else:
                    left +=1
                    continue
                left+=1
                right-=1
        return result  