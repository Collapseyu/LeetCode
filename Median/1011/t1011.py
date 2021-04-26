from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        max_v = sum(weights)
        min_v = max(weights)
        def v_d_check(v):
            day = 0
            sum_value = 0
            for i in weights:
                if sum_value + i > v:
                    day += 1
                    if day > D:
                        return False
                    sum_value = i
                else:
                    sum_value += i
            if day + 1 > D:
                return False
            return True
        while(max_v >= min_v):
            mid = (max_v+min_v)//2
            if v_d_check(mid):
                max_v = mid - 1
            else:
                min_v = mid + 1
        return min_v