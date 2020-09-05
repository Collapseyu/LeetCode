from typing import List
class Solution:
    def maxProfit_dp(self, prices: List[int]) -> int:
        pricesLength=len(prices)
        dp =[[-1 for x in range(2)] for y in range(pricesLength)]
        dp[0][0]=0
        dp[0][1]=-prices[0]

        for i in range(1,pricesLength):
            dp[i][0]=max(dp[i-1][1]+prices[i],dp[i-1][0])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
        
        return dp[-1][0]
    def maxProfit_regular(self,prices:List[int]) -> int:
        buyFlag=False
        pricesLen=len(prices)
        inprice=0
        res=0
        for i in range(pricesLen-1):
            if prices[i]<prices[i+1] and buyFlag==False:
                buyFlag=True
                inprice=prices[i]
                continue
            if buyFlag==True and prices[i]>prices[i+1]:
                buyFlag=False
                res+=(prices[i]-inprice)
        if buyFlag==True:
            res+=(prices[-1]-inprice)
        return res