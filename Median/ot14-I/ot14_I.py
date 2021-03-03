from typing import List
import math
class Solution:
    def cuttingRope(self, n: int) -> int:
        if n < 4:
            return n - 1
        dp = [1 for _ in range(n+1)]
        for i in range(3,n+1):
            for j in range(1,i-1):
                dp[i] = max((i-j)*dp[j],dp[i])
            dp[i] = max(dp[i],i)
        # print(dp)
        return dp[-1]
    def cuttingRope_greedy(self,n:int) -> int:
        if n<=3:
            return n-1
        tmp_n = (n//3) - 1
        left_num = (n%3)
        res = int(math.pow(3,tmp_n))
        if 3 - left_num > left_num:
            res *= (3+left_num)
        else:
            res *= (left_num*3)
        return res
        