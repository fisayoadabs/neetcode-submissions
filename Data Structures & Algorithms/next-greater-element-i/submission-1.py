class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for i in nums1:
            found = False
            for j in range(len(nums2)):
                if nums2[j] == i:
                    for k in range(j + 1,len(nums2)):
                        if nums2[k] > i:
                            result.append(nums2[k])
                            found = True
                            break
                    break
            if not found:
                result.append(-1)
        return result
        