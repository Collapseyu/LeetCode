from typing import List
class NumArray:

    def __init__(self, nums: List[int]):
        self.dp = [0 for i in range(len(nums)+1)]
        self.dp[0] = 0
        for i in range(len(nums)):
            self.dp[i+1] = nums[i] + self.dp[i]
        # print(self.dp)

            


    def sumRange(self, i: int, j: int) -> int:
        return self.dp[j+1] - self.dp[i]