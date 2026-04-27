class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        profit = 0
        for i in prices:
            min_price = min(min_price, i)
            delta = i - min_price
            profit = max(delta, profit)
        return profit


        