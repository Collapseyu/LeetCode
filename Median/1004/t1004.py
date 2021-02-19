from typing import List
class Solution:
    def process(self,ptr,static_list,tmpK):
        # print(ptr,static_list,tmpK)
        if len(static_list) < 2:
            return static_list[0] + tmpK
        if tmpK + static_list[ptr] < 0:
            if ptr - 1 >= 0: 
                return max(static_list[ptr-1],static_list[ptr+1]) + tmpK
            else:
                return static_list[ptr+1] + tmpK
        else:
            # if ptr - 1 > 0:
            cur = static_list[ptr-1] + static_list[ptr+1] - static_list[ptr]
            tmpK += static_list[ptr]
            if ptr + 2 > len(static_list):
                return cur
            else:
                tmp_list = static_list[ptr+2:]
                tmp_list.insert(0,cur)
                # print(tmp_list)
                return self.process(1,tmp_list,tmpK)

    def longestOnes(self, A: List[int], K: int) -> int:
        static_list = []
        tmp_one = 0
        tmp_zero = 0
        total_zero = 0
        for i in range(len(A)):
            if A[i] == 0:
                tmp_zero -= 1
                if tmp_one > 0:
                    static_list.append(tmp_one)
                    tmp_one = 0
            elif A[i] == 1:
                tmp_one += 1
                if tmp_zero < 0:
                    static_list.append(tmp_zero)
                    total_zero -= tmp_zero
                    tmp_zero = 0
        if tmp_zero < 0 :
            static_list.append(tmp_zero)
            total_zero -= tmp_zero
        if tmp_one > 0:
            static_list.append(tmp_one)
        if total_zero < K:
            return len(A)
        if static_list[0] < 0:
            static_list.insert(0,0)
        if static_list[-1] < 0:
            static_list.append(0)
        res = 0
        ptr = 1
        # print(self.process(1,static_list,K))
        # print(static_list)
        while(ptr < len(static_list)):
            res = max(res,self.process(ptr,static_list,K))
            # print('cur res: ', res)
            ptr += 2
        return res
    def longestOnes_slide_windows(self, A: List[int], K: int) -> int:
        ptrL = 0
        ptrR = 0
        res = 0
        tmpK = K
        while(ptrR<len(A) and ptrL<len(A)):
            if (A[ptrR] == 1) or (A[ptrR]==0 and tmpK>0):
                if A[ptrR] == 0:
                    tmpK -= 1
                res = max(ptrR - ptrL + 1,res)
                ptrR += 1
            else:
                while(A[ptrL] != 0 and ptrL <= ptrR):
                    ptrL += 1
                if tmpK < K:
                    tmpK += 1 
                ptrL += 1
                if ptrR < ptrL:
                    ptrR = ptrL
        return res
    def longestOnes_simple(self, A: List[int], K: int) -> int:
        ptrL,ptrR,tmpK = 0,0,0
        while(ptrR<len(A)):
            if A[ptrR] == 0:
                tmpK += 1
            if tmpK > K:
                if A[ptrL] == 0:
                    tmpK -= 1
                ptrL += 1
            ptrR += 1
        return ptrR - ptrL