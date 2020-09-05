class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        dur=n-1
        total=k-1
        inNum=0
        stillNum=0
        res=""
        candidate =[str(i) for i in range(1,n+1)]
        # print(candidate)
        def A(nCan):
            res=1
            for i in range(1,nCan+1):
                res*=i
            return res
        while(total>=1):
            whileDur=A(dur)
            inNum=(total//whileDur)
            total=total%whileDur
            print(candidate)
            print(inNum)
            dur-=1
            res+=candidate[inNum]
            del candidate[inNum]
        for i in candidate:
            res+=i
        return res