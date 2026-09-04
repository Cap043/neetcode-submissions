class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # diff=[]
        # for i in range(len(prices)-1):
        #     for j in range(i,len(prices)):
        #         diff.append(prices[j]-prices[i])
        # return max(diff)
        max_profit=0
        buy=0
        sell=1
        while sell<len(prices):
            if prices[buy]<prices[sell]:
                profit=prices[sell]-prices[buy]
                max_profit=max(max_profit,profit)
            else:
                buy=sell
            sell+=1
        return max_profit

