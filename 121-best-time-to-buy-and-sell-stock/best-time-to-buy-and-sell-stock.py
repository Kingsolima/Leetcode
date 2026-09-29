class Solution:
    """
    brute: 
    profit = 0
    for i in range loop:
        buy = [i]
        for j in range loop:
            sell = [j]
            if profit < sell-buy
                profit = sell - buy
    return profit
    """
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_profit=0
        while r < len(prices):
            if prices[r] > prices[l]:
                profit = prices[r]-prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1        
        return max_profit
        