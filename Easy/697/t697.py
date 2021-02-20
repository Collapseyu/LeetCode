from typing import List
class Solution:
    def get_sub_length(self,value,nums):
        ptrL = 0 
        ptrR = 0
        firstFlag = True
        for i in range(len(nums)):
            if nums[i] == value:
                if firstFlag:
                    firstFlag = False
                    ptrL = i
                ptrR = i
        return ptrR - ptrL + 1
    def findShortestSubArray_first(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        freq_max_num = []
        freq_max = 0
        tmp_num = sort_nums[0]
        tmp_count = 1
        for i in range(1,len(sort_nums)):
            # print(sort_nums[i],tmp_num,tmp_count,freq_max)
            if sort_nums[i] == tmp_num:
                tmp_count += 1
            else:
                if tmp_count == freq_max:
                    freq_max_num.append(tmp_num)
                elif tmp_count > freq_max:
                    freq_max_num = []
                    freq_max_num.append(tmp_num)
                    freq_max = tmp_count
                tmp_num = sort_nums[i]
                tmp_count = 1
        if tmp_count == freq_max:
            freq_max_num.append(tmp_num)
        elif tmp_count > freq_max:
            freq_max_num = []
            freq_max_num.append(tmp_num)
            freq_max = tmp_count
        res = 50001
        for i in freq_max_num:
            res = min(self.get_sub_length(i,nums),res)
        return res
    def findShortestSubArray(self,nums:List[int]) -> int:
        hashdict = {}
        max_count = 0
        max_num = []
        for i in range(len(nums)):
            if nums[i] not in hashdict.keys():
                hashdict[nums[i]] = [1,i,i]
            else:
                hashdict[nums[i]][0] += 1
                hashdict[nums[i]][2] = i
            if hashdict[nums[i]][0] == max_count:
                max_num.append(nums[i])
            elif hashdict[nums[i]][0] > max_count:
                max_num = []
                max_num.append(nums[i])
                max_count = hashdict[nums[i]][0]
        res = 50001
        for i in max_num:
            res = min(res,hashdict[i][2]-hashdict[i][1]+1)
        return res