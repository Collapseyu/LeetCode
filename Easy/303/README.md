# 区域和检索 - 数组不可变
## 题目简介
###   
给定一个整数数组  nums，求出数组从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点。  
实现 NumArray 类：  
NumArray(int[] nums) 使用数组 nums 初始化对象  
int sumRange(int i, int j) 返回数组 nums 从索引 i 到 j（i ≤ j）范围内元素的总和，包含 i、j 两点（也就是 sum(nums[i], nums[i + 1], ... , nums[j])）
## 示例：  
### 1  
输入：  
["NumArray", "sumRange", "sumRange", "sumRange"]  
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]  
输出：  
[null, 1, -1, -3]  
## 解题思路
### Step 1：  
拿到题的第一个想法是用一个[2,len(nums)]的数组存下包含节点的值和不包含节点的值这两种情况，但冷静分析了一下发现不需要，因为如果用一维数组表示包含节点的值来表示数组，则可以用前一位的数字来表示
不包含该位的sum。之后就很简单了，统计一下至每个数字的sum总和，在init的时候存起来。在sumrRange的时候只需要拿两位减一下就成。时间复杂度在init的时候是O(N)，在sumrange的时候就是O(1)了。
