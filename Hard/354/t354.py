from typing import List
class Solution:
    def maxEnvelopes_overtime(self, envelopes: List[List[int]]) -> int:
        hash_dict = {}
        key_list = []
        for i in envelopes:
            if i[0] not in hash_dict.keys():
                hash_dict[i[0]] = [[i[1],1]]
                newFlag = True
                for j in range(len(key_list)):
                    if i[0]<key_list[j]:
                        key_list.insert(j,i[0])
                        newFlag = False
                        break
                if newFlag:
                    key_list.append(i[0])
            else:
                addFlag = True
                for j in range(len(hash_dict[i[0]])):
                    if i[1]<hash_dict[i[0]][j][0]:
                        hash_dict[i[0]].insert(j,[i[1],1])
                        addFlag = False
                        break
                if addFlag:
                    hash_dict[i[0]].append([i[1],1])
        # print(hash_dict)
        # print(key_list)
        # ptrL = 0 
        # ptrR = 0
        res = 1
        for i in range(1,len(key_list)):
            start_index = len(hash_dict[key_list[i-1]]) - 1
            for j in range(i):
                start_index = len(hash_dict[key_list[j]]) - 1
                for x in range(len(hash_dict[key_list[i]]) - 1,-1,-1):
                    flag = False
                    for y in range(start_index,-1,-1):
                        if hash_dict[key_list[j]][y][0] < hash_dict[key_list[i]][x][0]:
                            start_index = y
                            tmp = 1 + hash_dict[key_list[j]][y][1]
                            hash_dict[key_list[i]][x][1] = max(hash_dict[key_list[i]][x][1],tmp)
                            res = max(hash_dict[key_list[i]][x][1],res)
                            flag = True
                            break
                        if not flag:
                            start_index = 0
        
        # print(hash_dict)
        return res


        # envelopes.sort(key = lambda x:x[0])
    def maxEnvelopes_binary_search(self, envelopes: List[List[int]]) -> int:
        def binary_search(num_list,start,end,target,single):
            # print(num_list,start,end,target)
            if len(num_list) == 0:
                return 0
            while(start <= end):
                mid = (start + end)//2
                if single:
                    judge_num = num_list[mid]
                else:
                    judge_num = num_list[mid][0]
                if judge_num >= target:
                    end = mid - 1
                else:
                    start = mid + 1
            return start
        hash_dict = {}
        key_list = []
        for i in envelopes:
            # print(i)
            if i[0] not in hash_dict.keys():
                hash_dict[i[0]] = [[i[1],1]]
                index = binary_search(key_list,0,len(key_list)-1,i[0],True)
                key_list.insert(index,i[0])
            else:
                index = binary_search(hash_dict[i[0]],0,len(hash_dict[i[0]])-1,i[1],False)
                hash_dict[i[0]].insert(index,[i[1],1])
        # print(hash_dict)
        # print(key_list)
        # ptrL = 0 
        # ptrR = 0
        res = 1
        for i in range(1,len(key_list)):
            start_index = len(hash_dict[key_list[i-1]]) - 1
            for j in range(i):
                index = len(hash_dict[key_list[j]])
                for x in range(len(hash_dict[key_list[i]]) - 1,-1,-1):
                    flag = False
                    index = binary_search(hash_dict[key_list[j]],0,index - 1,hash_dict[key_list[i]][x][0],False)
                    if index > 0:
                        hash_dict[key_list[i]][x][1] = max(hash_dict[key_list[i]][x][1],1 + hash_dict[key_list[j]][index-1][1])
                    else:
                        break
        for i in hash_dict.keys():
            for j in hash_dict[i]:
                res = max(res,j[1])
        # print(hash_dict)
        return res
    def maxEnvelopes_simpledp(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
    
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        dp = [1] * n
        res = 1
        for i in range(n):
            for j in range(i):
                if envelopes[i][1]>envelopes[j][1]:
                    dp[i] = max(dp[i],dp[j]+1)
                    res = max(res,dp[i])
        return res
    def maxEnvelopes_binarydp(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        
        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        f = [envelopes[0][1]]
        for i in range(1, n):
            num = envelopes[i][1]
            if num > f[-1]:
                f.append(num)
            else:
                index = bisect.bisect_left(f, num)
                f[index] = num
        
        return len(f)