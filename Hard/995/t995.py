from typing import List
class Solution:
    def minKBitFlips(self, A: List[int], K: int) -> int:
        res = 0
        cur_rev = 0
        A.append(0)
        for i in range(len(A)-1):
            if A[i] >= 2:
                cur_rev ^= 1
                A[i] -= 2
            if A[i] == cur_rev:
                if i+K > len(A)-1:
                    return -1 
                res += 1
                cur_rev ^= 1
                A[i+K] += 2
        return res
