from typing import List
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