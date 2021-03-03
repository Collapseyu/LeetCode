import math
from typing import List
class Solution:
    def cuttingRope(self, n: int) -> int:
        # 快速幂求余
        def remainder(x, a, p):
            rem = 1
            while a > 0:
                if a % 2: rem = (rem * x) % p
                x = x ** 2 % p
                a //= 2
            return rem
        if n<= 3:
            return n-1
        tmp_n = (n//3) - 1
        left_num = (n%3) 
        res =  remainder(3,tmp_n,1000000007)
        if 3 - left_num > left_num:
            res *= (3+left_num)
            res = res % 1000000007
        else:
            res *= (left_num*3) 
            res = res % 1000000007
        return res