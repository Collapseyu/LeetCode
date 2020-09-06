from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        candiatList=[root]
        oldLayerNum=1
        newLayerNum=0
        res=[]
        if root==None:
            return res
        durRes=[]
        count=0
        flag=0
        while(len(candiatList)!=0):
            nowNode=candiatList[0]
            durRes.append(nowNode.val)
            count+=1
            del candiatList[0]
            if nowNode.left != None:
                candiatList.append(nowNode.left)
                newLayerNum+=1
            if nowNode.right!= None:
                candiatList.append(nowNode.right)
                newLayerNum+=1
            if count==oldLayerNum:
                res.append(durRes)
                durRes=[]
                count=0
                oldLayerNum=newLayerNum
                newLayerNum=0
        res.reverse()
        return res