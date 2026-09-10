class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        result = 0
        for i in prices:
            if i < minPrice:
                minPrice = i
            result = max(i-minPrice, result)
        return result