import sys,os
struct_path = 'D:\\yuyicong\\workspace\\Algorithm_\\method'
sys.path.append(struct_path)
from structAndBuild import *

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse_list(l):
            start = l
            ptr_last = l
            ptr = l.next
            while(ptr):
                tmp = ptr
                tmp_last = ptr_last

                ptr_last = ptr
                ptr = ptr.next

                tmp.next = tmp_last
            start.next = None
            return ptr_last
        if not head:
            return head
        count = 0
        new_head = ListNode(-1)
        ptr = head
        block_out_last = new_head
        block_in_last = None
        while(ptr):
            count += 1
            if count == 1:
                end = ptr
                block_in_last = ptr
                ptr = ptr.next
            elif count <= k:
                tmp = ptr  #ptr 2
                ptr = ptr.next  #ptr 3
                tmp.next = block_in_last # 2->1
                block_in_last = tmp # 2
            if count == k:
                block_out_last.next = block_in_last 
                block_out_last = end
                count = 0
#         block_out_last.next = block_in_last
        end.next = None 
        if count != 0:
            block_out_last.next = reverse_list(block_in_last)
            
        return new_head.next