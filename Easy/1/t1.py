class Solution:
    def twoSum(self, nums, target):
        hashMap={}
        for index,num in enumerate(nums):
            anotherNum=target-num
            if anotherNum in hashMap:
                return [hashMap[anotherNum],index]
            hashMap[num]=index
        return null