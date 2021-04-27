import sys,os
struct_path = 'D:\\yuyicong\\workspace\\Algorithm_\\method'
sys.path.append(struct_path)
from structAndBuild import *
import test_frame

from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        min_val = float('inf')
        for i in nums:
            if i < min_val:
                min_val = i
        return sum(nums) - min_val*len(nums)