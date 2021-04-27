import sys,os
struct_path = 'D:\\yuyicong\\workspace\\Algorithm_\\method'
sys.path.append(struct_path)
from structAndBuild import *

from typing import List

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        res = 0
        def dfs(node):
            nonlocal res
            if not node:
                return
            if low <= node.val <=high:
                res += node.val
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res