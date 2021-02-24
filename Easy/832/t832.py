from typing import List
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        line_len = len(A[0])
        line_flag = ((line_len%2) == 1)
        for i in range(len(A)):
            for j in range(line_len//2):
                tmp =  1 - A[i][j]
                # print(tmp)
                A[i][j] = 1 - A[i][line_len-1-j]
                A[i][line_len-1-j] = tmp
            if line_flag:
                A[i][line_len//2] = 1 - A[i][line_len//2]
        return A