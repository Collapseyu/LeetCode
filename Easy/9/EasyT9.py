class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        intList=[]
        while x>0:
            intList.append(x%10)
            # print(x%10)
            x//=10
        print(intList)
        ptrA=0
        ptrB=len(intList)-1
        while(ptrB>ptrA):
            if intList[ptrA]==intList[ptrB]:
                ptrA+=1
                ptrB-=1
            else:
                return False
        return True