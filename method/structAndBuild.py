class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeStruct_process:
    def __init__(self):
        pass
    def buildFromList_complete(self,node_val_list):
        # 需要输入一个完整的层次遍历列表 所有null值不能省略
        node_list = []
        for i in range(len(node_val_list)):
            if node_val_list[i] == 'null':
                node_list.append(None)
            else:
                node_list.append(TreeNode(node_val_list[i]))
            if (i-1) >= 0:
                father = (i-1)//2
                if not node_list[father]:
                    continue
                if (i-1)%2 == 0:
                    node_list[father].left = node_list[i]
                else:
                    node_list[father].right = node_list[i]
        return node_list
    def buildFromList_uncomplete(self,node_val_list):
        # leetcode 给出的列表，若上层节点为None，则下层不会再输出None
        node_list = []
        empty_list = []
        for i in range(len(node_val_list)):
            while len(empty_list)>0 and (len(node_list)) == empty_list[0]:
                del empty_list[0]
                node_list.append(None)
            if node_val_list[i] == 'null':
                node_list.append(None)
                empty_list.append(i*2+1)
                empty_list.append(i*2+2)
            else:
                node_list.append(TreeNode(node_val_list[i]))
            ptr = len(node_list) - 1
            if (ptr - 1) >= 0:
                father = (ptr - 1)//2
#                 print(father)
                if not node_list[father]:
                    continue
                if (ptr - 1)%2 == 0:
                    node_list[father].left = node_list[ptr]
                else:
                    node_list[father].right = node_list[ptr]
        return node_list
    def treeNode_list_val_print(self,tree_node_list):
        def print_judge(x):
            if x != None:
                return x.val
            else:
                return x
        res = list(map(print_judge,tree_node_list))
        print(res)
        return res
    def show_uncomplete_val_list(self,node):
        res = []
        queue = [node]
        last_index = 0
        while len(queue)>0:
            tmp = queue[0]

            del queue[0]
            if tmp == None:
                res.append('null')
                continue
            else:
                exist_flag = True
                res.append(tmp.val)
                last_index = len(res)
                queue.append(tmp.left)
                queue.append(tmp.right)


        return res[:last_index]
    def frontOrder(self,root):
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
            return
        dfs(root)
        return res
    def inOrder(self,root):
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
            return
        dfs(root)
        return res
    def backOrder(self,root):
        res = []
        def dfs(node):
            nonlocal res
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
            return
        dfs(root)
        return res
    
class listNode_struct:
    def __init__(self):
        pass
    def build_listNode_from_valList(self,val_list):
        if len(val_list) == 0:
            return None
        list_example = ListNode(val_list[0])
        ptr = list_example
        for i in range(1,len(val_list)):
            ptr.next = ListNode(val_list[i])
            ptr = ptr.next
        return list_example
    def list_show(self,node_list):
        #todo list_show方法现在没有考虑循环列表
        res = []
        while(node_list):
            res.append(node_list.val)
            node_list = node_list.next
        return res
    

