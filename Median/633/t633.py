from typing import List
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_sub_value = int(math.sqrt(c))
        min_sub_value = 0
        while(max_sub_value >= min_sub_value):
#             print(max_sub_value,min_sub_value)
            tmp = max_sub_value**2 + min_sub_value**2
            if tmp == c:
                return True
            elif tmp > c:
                max_sub_value -= 1
            else:
                min_sub_value += 1
        return False