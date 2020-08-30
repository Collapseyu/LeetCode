class Solution:
    def reverseWords(self, s: str) -> str:
        
        splitList=s.split()
        res=""
        for i in range(len(splitList)):
            lenth=len(splitList[i])
            for j in range(0,lenth):
                res+=splitList[i][lenth-1-j]
            if i!=len(splitList)-1:
                res+=' '
        return res
    def reverseWords_method1(self,s:str) ->str:
        s=s[::-1]
        s=s.split()
        s.reverse()
        return ' '.join(s)