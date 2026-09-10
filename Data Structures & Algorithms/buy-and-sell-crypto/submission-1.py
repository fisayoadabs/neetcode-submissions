class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for i in range(len(prices)):
            pointer = i + 1
            while pointer < len(prices):
                result = max(prices[pointer]-prices[i], result)
                pointer +=1
        return result