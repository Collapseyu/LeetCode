from typing import List
class Solution:
    def strStr(self,s: str,p: str) -> int:
        i,j = 0,0
        m,n = len(s), len(p)
        nxt = self.nxt_pos(p)
        while i<m and j<n:
            # 注意 一定要有j=-1
            if j==-1 or s[i]==p[j]: 
                i+=1
                j+=1
            else:
                j=nxt[j]
        return i-n if j==n else -1
    # next[i]表示p的前i个字符组成的子串p[0,..,i-1]的最长公共前后缀长度 
    def nxt_pos(self, p):
        n=len(p)
        nxt = [-1]+[0]*n
        for i in range(2,n+1):
            j=nxt[i-1]
            while p[i-1]!=p[j] and j!=-1: #注意 是and
                j=nxt[j]
            nxt[i]=j+1
        return nxt