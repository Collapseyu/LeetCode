import math
from typing import List
class Solution:
    def countBits_ori(self, num: int) -> List[int]:
        # [0,1,10,11,100,101,110,111,1000,1001,1010,1011]
        # [0,1,1,2,1,2,2,3,1,2,2,3,2,]
        tmp_n = 0
        res = [0]
        ptr = 1
        while(ptr <= num):
            if ptr == math.pow(2,tmp_n):
                res.append(1)
                tmp_n += 1
            else:
                res.append(res[ptr - int(math.pow(2,tmp_n-1))]+1) 
            ptr += 1
        return res
    def countBits_simple(self, num: int) -> List[int]:
        res = [0] * (num+1)
        res[0] = 0
        for i in range(1,num+1):
            res[i] = res[i//2] + (i&1)
        return res 
