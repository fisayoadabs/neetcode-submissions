class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        result = 0
        for i in prices:
            if i < minPrice:
                minPrice = i
            profit = i - minPrice
            if result < profit:
                result = profit
        return result