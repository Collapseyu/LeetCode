from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap={}
        for i in nums:
            if i in hashMap:
                hashMap[i]+=1
            else:
                hashMap[i]=1
        hashMap = sorted(hashMap.items(), key=lambda x:x[1], reverse = True)
        print(hashMap)
        count=0
        res=[]
        for v in hashMap:
            if count==k:
                break
            print(v[0])
            res.append(v[0])
            count+=1
        return res
