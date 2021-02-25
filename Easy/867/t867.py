from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [ [] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res[j].append(matrix[i][j])
        return res