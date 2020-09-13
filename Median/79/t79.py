from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dimOne=max(list(map(len,board)))
        dimZero=len(board)
        flagMatrix=[[0 for i in range(dimOne)] for j in range(dimZero)]
        ptrSerachA=0
        ptrSerachB=0
        ptrWord=0
        wordLen=len(word)
        totalRes=False
        def recall(board,flagMatrix,ptrA,ptrB,word,ptrW):
            res=False
            if board[ptrA][ptrB]==word[ptrW]:
                flagMatrix[ptrA][ptrB]=1
                if ptrW==wordLen-1:
                    return True
                if ptrA-1>=0 and flagMatrix[ptrA-1][ptrB]==0:
                    res=res|recall(board,flagMatrix,ptrA-1,ptrB,word,ptrW+1)
                    if res==True:
                        return res
                if ptrA+1<len(board) and flagMatrix[ptrA+1][ptrB]==0:
                    res=res|recall(board,flagMatrix,ptrA+1,ptrB,word,ptrW+1)
                    if res==True:
                        return res
                if ptrB-1>=0 and flagMatrix[ptrA][ptrB-1]==0:
                    res=res|recall(board,flagMatrix,ptrA,ptrB-1,word,ptrW+1)
                    if res==True:
                        return res
                if ptrB+1<len(board[ptrA]) and flagMatrix[ptrA][ptrB+1]==0:
                    res=res|recall(board,flagMatrix,ptrA,ptrB+1,word,ptrW+1)
                    if res==True:
                        return res
                flagMatrix[ptrA][ptrB]=0
            return res
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]==word[0]:
                    totalRes=totalRes|recall(board,flagMatrix,i,j,word,0)
                    if totalRes==True:
                        return totalRes
        return totalRes