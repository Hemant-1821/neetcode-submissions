class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0

        i, j = 0,1 
        max_profit = 0
        while i < len(prices)-1 and j < len(prices):
            curr_profit = prices[j] - prices[i]
            if(curr_profit > max_profit):
                max_profit = curr_profit
                j += 1
                continue
                        
            if prices[i] > prices[j]:
                i = j
                j += 1
            else:
                j += 1  

        return max_profit
        