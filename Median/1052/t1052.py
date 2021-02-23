from typing import List
class Solution:
    def maxSatisfied_cal_total(self, customers: List[int], grumpy: List[int], X: int) -> int:
        ptrL = 0
        ptrR = 0
        improve_value = 0
        total_value = 0
        while(ptrR - ptrL < X ):
            if grumpy[ptrR] == 0:
                total_value += customers[ptrR]
            else:
                improve_value += customers[ptrR]
            ptrR += 1
        # print(improve_value,total_value)
        tmp = improve_value
        while(ptrR<len(customers)):
            if grumpy[ptrR] == 0:
                total_value += customers[ptrR]
            else:
                tmp += customers[ptrR]
            ptrR += 1
            if grumpy[ptrL] ==1:
                tmp -= customers[ptrL]
            ptrL += 1
            if tmp > improve_value:
                improve_value = tmp
            # print(ptrL,ptrR,improve_value,total_value)
        # print(improve_value,total_value)
        return improve_value+total_value