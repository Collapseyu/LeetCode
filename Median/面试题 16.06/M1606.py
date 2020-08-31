from typing import List
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a=sorted(a)
        b=sorted(b)
        
        ptrA=0
        ptrB=0
        lengthA=len(a)
        lengthB=len(b)

        res=abs(a[0]-b[0])

        while(ptrA<lengthA and ptrB<lengthB):
            durRes=a[ptrA]-b[ptrB]
            if abs(durRes)<res:
                res=abs(durRes)
            if durRes==0:
                return res
            elif durRes<0:
                ptrA+=1
            else:
                ptrB+=1
        return res