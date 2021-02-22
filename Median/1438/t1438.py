from typing import List
class Solution:
    def binary_search(self,sort_list,value):
        ptrL = 0
        ptrR = len(sort_list) - 1
        while(ptrL<ptrR):
            mid = ( ptrL + ptrR ) // 2
            if sort_list[mid] == value:
                return mid
            elif sort_list[mid] > value:
                ptrR = mid - 1
            else:
                ptrL = mid + 1
        return ptrL
    def sort_list_insert(self,sort_list,value):
        for i in range(len(sort_list)):
            if value < sort_list[i]:
                sort_list.insert(i,value)
                return sort_list
        sort_list.append(value)
        return sort_list
    def sort_list_del(self,sort_list,value):
        for i in range(len(sort_list)):
            if sort_list[i] == value:
                del sort_list[i]
                return sort_list
    def longestSubarray_overtime(self, nums: List[int], limit: int) -> int:
        ptrL = 0
        ptrR = 0
        
        sort_list = []

        while(ptrR<len(nums)):
            self.sort_list_insert(sort_list,nums[ptrR])
            if sort_list[-1] - sort_list[0] > limit:
                self.sort_list_del(sort_list,nums[ptrL])
                ptrL += 1
            ptrR += 1
        
        return ptrR - ptrL
    def binary_search(self,sort_list,value):
        ptrL = 0
        ptrR = len(sort_list) - 1
        while(ptrL <= ptrR):
            mid = ( ptrL + ptrR ) // 2
            if sort_list[mid] == value:
                return mid
            elif sort_list[mid] > value:
                ptrR = mid - 1
            else:
                ptrL = mid + 1
        return ptrL
    def sort_list_binary_insert(self,sort_list,value):
        index = self.binary_search(sort_list,value)
        sort_list.insert(index,value)
        return sort_list
    def sort_list_binary_del(self,sort_list,value):
        index = self.binary_search(sort_list,value)
        del sort_list[index]
        return sort_list
    def longestSubarray_binary(self, nums: List[int], limit: int) -> int:
        ptrL = 0
        ptrR = 0
        
        sort_list = []

        while(ptrR<len(nums)):
            self.sort_list_binary_insert(sort_list,nums[ptrR])
            
            if sort_list[-1] - sort_list[0] > limit:
                self.sort_list_binary_del(sort_list,nums[ptrL])
                ptrL += 1
            ptrR += 1
            # print(sort_list,ptrL,ptrR)
        # print(ptrR,ptrL)
        return ptrR - ptrL
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minList = []
        maxList = []
        l = 0 
        r = 0
        while(r < len(nums)):
            # print('front: ',maxList,minList)
            while(len(minList) != 0 and nums[r] < minList[-1]):
                minList.pop()
            while(len(maxList) != 0 and nums[r] > maxList[-1]):
                maxList.pop()
            minList.append(nums[r])
            maxList.append(nums[r])
            # print('mid: ',maxList,minList,l,r)
            if len(minList) != 0 and len(maxList) != 0 and maxList[0]-minList[0] > limit:
                if nums[l] == maxList[0]:
                    del maxList[0]
                    # print('del success')
                if nums[l] == minList[0]:
                    del minList[0]
                l += 1
            r += 1
            # print('after: ',maxList,minList)
        # print(l,r)
        return r - l