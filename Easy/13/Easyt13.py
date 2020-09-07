class Solution:
    def romanToInt(self, s: str) -> int:
        doubleCharList={'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        singleCharList={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        length=len(s)
        res=0
        ptr=0
        while ptr<length:
            print(ptr)
            if ptr+1<length:
                if s[ptr:ptr+2] in doubleCharList:
                    res+=doubleCharList[s[ptr:ptr+2]]
                    ptr+=2
                    continue
            res+=singleCharList[s[ptr]]
            ptr+=1
        return res