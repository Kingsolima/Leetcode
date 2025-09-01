class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = prices[0]
        output = 0
        for i in range (1, len(prices)):
            if prices [i]<low:
                low = prices[i]
            if prices[i]-low>output:
                output = prices[i]-low
        return output

            