import structAndBuild
class Test_Frame:
    # 目前不支持如 [1,3,2] 和 [1,2,3]是等价的情况
    # todo 树结构支持 链表结构支持
    def __init__(self,examples,ans,args_count,solution,
                 in_List_need = False,in_Tree_need = False,
                 out_List_need = False,out_Tree_need = False,
                 tree_convert_complete = False, tree_or_list_index = 0):
        self.examples = examples
        self.ans = ans
        self.args_count = args_count
        self.args_index = [i for i in range(args_count)]
        self.solution = solution
        
        self.in_List_need = in_List_need
        self.in_Tree_need = in_Tree_need
        self.out_List_need = out_List_need
        self.out_Tree_need = out_Tree_need
        self.tree_convert_complete = tree_convert_complete
        self.tree_or_list_index = tree_or_list_index
        
        # 链表处理模块 把用列表表示的链表转换成真实链表
        def list_process(x):
            if self.args_count == 1:
                x = [self.lns.build_listNode_from_valList(x)]
            else:
                x[self.tree_or_list_index] = self.lns.build_listNode_from_valList(x[self.tree_or_list_index])
            return x
        if self.in_List_need or self.out_List_need: 
            self.lns = structAndBuild.listNode_struct()
        if self.in_List_need:
            self.examples = list(map(list_process,self.examples))
        
        # 树处理模块 把用列表表示的树转换成真实的树结构
        def tree_process_complete(x):
            if self.args_count == 1:
                x = [self.tsp.buildFromList_complete(x)[0]]
            else:
                x[self.tree_or_list_index] = self.tsp.buildFromList_complete(x[self.tree_or_list_index])[0]
            return x
        def tree_process_uncomplete(x):
            if self.args_count == 1:
                x = [self.tsp.buildFromList_uncomplete(x)[0]]
            else:
                x[self.tree_or_list_index] = self.tsp.buildFromList_uncomplete(x[self.tree_or_list_index])[0]
            return x
        if self.in_Tree_need or self.out_Tree_need:
            self.tsp = structAndBuild.TreeStruct_process()
        if self.in_Tree_need:
            if self.tree_convert_complete:
                self.examples = list(map(tree_process_complete,self.examples))
            else:
                self.examples = list(map(tree_process_uncomplete,self.examples))
        
    def check_algorithm(self):
        flag = True
        for index,(example,single_ans) in enumerate(zip(self.examples,self.ans)):
            arg = list(map(lambda x:example[x],self.args_index))
            res = self.solution(*arg)
            # 偷懒的方法 把链表再转成List 
            if self.out_List_need:
                res = self.lns.list_show(res)
            if self.out_Tree_need:
                if self.tree_convert_complete:
                    print('complete compare is not supported yet')
                    return
                else:
                    res = self.tsp.show_uncomplete_val_list(res)
            if res != single_ans:
                flag = False
                print('index ',index,' error')
                print('algorithm output is: ',res)
                print('real ans is: ',single_ans)
        if flag:
            print('All the contained tests passed')
        return
            
        