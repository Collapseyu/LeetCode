class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res=[]
        def recall(node):
            if node == None:
                return
            if node.left!=None:
                recall(node.left)
            res.append(node.val)
            if node.right!=None:
                recall(node.right)
        recall(root)
        return res