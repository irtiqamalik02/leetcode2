class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # l: buy, r:sell
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r # shift to the min position
            r += 1 # move r regardless

        return maxProfit    


        