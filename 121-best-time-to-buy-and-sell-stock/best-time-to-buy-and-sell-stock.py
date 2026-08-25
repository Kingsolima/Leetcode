class Solution:
    """
    optimal: 

    Input = array of prices
    output = profit or 0

    method: use a nested for loop that has two pointers and has a max variable so that it checks for every difference calculated it goes through an if statement to determine if that is the max profit, else 0.

    time: o(n)
    space: o(1)
    """
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        low = prices[0]
        for i in range(len(prices)):
            if low > prices[i]:
                low = prices[i]
                continue
            difference = prices[i]-low
            if difference > max:
                max = difference
        if max == 0:
            return max
        return max

        