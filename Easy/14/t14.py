from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ptr=0
        resCommonprefix=""
        if len(strs)==0 or strs[0]=="":
            return resCommonprefix
        length=len(strs[0])
        while(ptr<length):
            commonPrefix=strs[0][ptr]
            for i in strs:
                if ptr==len(i) or i[ptr]!=commonPrefix:
                    return resCommonprefix
            resCommonprefix+=commonPrefix
            ptr+=1
        return resCommonprefix
    def longestCommonPrefix_mnlogm(self,strs:List[str])->str:
        def isCommonPrefix(length):
            str0, count = strs[0][:length], len(strs)
            return all(strs[i][:length] == str0 for i in range(1, count))

        if not strs:
            return ""

        minLength = min(len(s) for s in strs)
        low, high = 0, minLength
        while low < high:
            mid = (high - low + 1) // 2 + low
            if isCommonPrefix(mid):
                low = mid
            else:
                high = mid - 1

        return strs[0][:low]
