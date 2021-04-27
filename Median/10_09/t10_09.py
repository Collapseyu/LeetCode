import sys,os
struct_path = 'D:\\yuyicong\\workspace\\Algorithm_\\method'
sys.path.append(struct_path)
from structAndBuild import *
from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        x = 0
        y = len(matrix[0]) -1 
        while(x < len(matrix) and y >= 0):
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1
        return False