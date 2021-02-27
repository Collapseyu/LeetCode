from typing import List
class Solution:
    def longestSubstring_fenye(self, s: str, k: int) -> int:
        def find_error_index(s,k):
            hash_dict = {}
            for i in range(len(s)):
                if s[i] not in hash_dict.keys():
                    hash_dict[s[i]] = [1,[i]]
                else:
                    hash_dict[s[i]][0] += 1
                    hash_dict[s[i]][1].append(i)
            res = []
            for i in hash_dict.keys():
                if hash_dict[i][0]<k:
                    res.extend(hash_dict[i][1])
            # print(res)
            return sorted(res)
        # print(find_error_index(s,k))
        def find_max_sub(s,k):
            out_point = find_error_index(s,k)
            if len(out_point) == 0:
                return len(s)
            out_point.append(len(s))
            start = 0
            res = 0
            for i in out_point:
                # print(s,start,i)
                end = i
                if end - start < k-1:
                    pass
                else:
                    res = max(find_max_sub(s[start:end],k),res)
                start = end + 1
            # print(start)
            return res
        return find_max_sub(s,k)
    def longestSubstring_slide_window(self, s: str, k: int) -> int:
        res = 0
        max_ = min(27,len(s)+1)
        for t in range(1,max_):
            ptrR = 0
            ptrL = 0
            tot = 0
            less = 0
            count = [0 for _ in range(26)]
            while(ptrR<len(s)):
                # print('ptrR')
                # print(ptrR)
                count[ord(s[ptrR])-ord('a')] += 1
                if count[ord(s[ptrR])-ord('a')] == 1:
                    less += 1
                    tot += 1
                if count[ord(s[ptrR])-ord('a')] == k:
                    less -= 1
                ptrR += 1 
                # print('tot: ',tot)
                # print('less: ',less)
                # print('ptrL')
                while(tot>t):
                    # print(ptrL)
                    count[ord(s[ptrL])-ord('a')] -= 1
                    if count[ord(s[ptrL])-ord('a')] == k-1:
                        less += 1
                    if count[ord(s[ptrL])-ord('a')] == 0:
                        tot -= 1
                        less -= 1
                    # print('tot: ',tot)
                    # print('less: ',less)
                    ptrL += 1
                if less == 0:
                    res = max(res,ptrR-ptrL)
                    # print('res: ',res)
            if less == 0:
                res = max(res,ptrR - ptrL)
        return res
