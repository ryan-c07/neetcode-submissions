class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = prices[0]
        max = 0
        for i in range(len(prices)):
            if (prices[i] < buy):
                if (sell - buy > max):
                    max = sell - buy
                buy = prices[i]
                sell = prices[i]
            if (prices[i] > sell):
                sell = prices[i]
            print(buy, sell)
        if (sell - buy > max):
            max = sell - buy
        return max