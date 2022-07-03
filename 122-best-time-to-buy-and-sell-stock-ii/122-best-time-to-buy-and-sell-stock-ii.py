class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=0
        sell=0
        profit=0
        currprofit=0
        while sell<len(prices):
            if prices[sell]-prices[buy]>currprofit:
                currprofit=prices[sell]-prices[buy]
                sell+=1
                
            else:
                profit+=currprofit
                currprofit=0
                buy,sell=sell,sell+1
        profit+=currprofit
        return profit
                
        