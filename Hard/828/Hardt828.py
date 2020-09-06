class Solution:
    def uniqueCal(self,s):
        hashMap={}
        count=0
        for i in s:
            if i in hashMap:
                hashMap[i]+=1
            else:
                hashMap[i]=0
        for j in hashMap:
            if hashMap[j]==0:
                count+=1        
        return count    
    def uniqueLetterString(self, s: str) -> int:
        length=len(s)
        res=0
        for i in range(1,length+1):
#             mainHashMap={}
            ptr=0
            while((ptr+i)<=length):
                durStr=s[ptr:ptr+i]
                dur=self.uniqueCal(durStr)
                print('str: ',durStr,' res: ',dur)
                res+=dur
#                     mainHashMap[durStr]=0
                ptr+=1
        return res
    def uniqueLetterString_Mine(self,s: str) -> int: #700ms
        ptr=0
        length=len(s)
        res=0
        while(ptr<length):
            ptrA=ptr-1
            left=1
            while(ptrA>=0 and s[ptrA]!=s[ptr]):
                left+=1
                ptrA-=1
            ptrA=ptr+1
            right=1
            while(ptrA<length and s[ptrA]!=s[ptr]):
                right+=1
                ptrA+=1
            res+=left*right
            # print(res)
            ptr+=1
        return res
    def uniqueLetterString_best(self, s: str) -> int:
        index = {i: [-1, -1] for i in string.ascii_uppercase}
        res = 0
        for i, c in enumerate(s):
            a, b = index[c]
            res += (i - b) * (b - a)
            index[c] = [b, i]
        for i in index:
            a, b = index[i]
            res += (len(s) - b) * (b - a)
        return res % (10 ** 9 + 7)

\