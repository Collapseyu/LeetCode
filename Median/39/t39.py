from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def recall(candidates_,start,target_,subset):
            # print(subset)
            # print(target_)
            # print(candidates_[start])
            if target_==0:
                # subset.append(candidates_[start])
                res.append(subset[:])
                return
            elif target_<candidates[start]:
                return
            else:
                length=len(candidates_)
                while(start<length):
                    subset.append(candidates_[start])
                    recall(candidates_,start,target_-candidates_[start],subset)
                    subset.pop()
                    start+=1
                return
        candidates=sorted(candidates)
        recall(candidates,0,target,[])
        return res