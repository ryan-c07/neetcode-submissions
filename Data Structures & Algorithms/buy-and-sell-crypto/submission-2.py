class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        max = 0
        for price in prices:
            if buy > price:
                buy = price
                sell = price
            if sell < price:
                sell = price
                if sell - buy >= max:
                    max = sell - buy
        return max