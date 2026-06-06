class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        n = len(prices)

        for buy in range(n):
            for sell in range(buy + 1, n):
                max_profit = max(max_profit, prices[sell] - prices[buy])

        return max_profit