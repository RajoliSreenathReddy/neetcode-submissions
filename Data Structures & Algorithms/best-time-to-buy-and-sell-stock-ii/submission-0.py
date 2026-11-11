class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit=0
        min_price=float("inf")
        for i in range(len(prices)-1):
            if prices[i+1]>prices[i]:
                if prices[i]<min_price:
                    min_price=prices[i]
                total_profit+=prices[i+1]-min_price
                min_price=float("inf")
        return total_profit


            
