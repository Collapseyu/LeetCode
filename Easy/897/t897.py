import sys,os
struct_path = 'D:\\yuyicong\\workspace\\Algorithm_\\method'
sys.path.append(struct_path)
from structAndBuild import *

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.head = TreeNode(-1)
        self.tmp = self.head
        def inOrder(node):
            if node.left == None:
                if self.tmp == None:
                    self.tmp.right = node
                    self.tmp = self.tmp.right
            else:
                inOrder(node.left)
            node.left = None
            if self.tmp != node:
                self.tmp.right = node
                self.tmp = self.tmp.right
            if node.right != None:
                inOrder(node.right)
            # node.right = None
        inOrder(root)
        return self.head.right