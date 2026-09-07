class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l={}
        for i in range(len(prices)-1):
            l[i]=max(prices[i+1:len(prices)])-prices[i]
        l[len(prices)-1]=0
        return max(l.values())
        