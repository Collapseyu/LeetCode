# 比特位计数
## 题目描述  
### 给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
## 示例
### 1  
输入: 2  
输出: [0,1,1]  
### 2  
输入: 5  
输出: [0,1,1,2,1,2]  
## 解题思路  
### STEP 1  
最简单的思路是把每个小于等于num的值拉出来单独计算一下，缺点是耗时。实现也挺简单的，code里就没写
### STEP 2  
其实这个问题可以用动态规划的想法来解决，每次进到一个新的位数（1，2，4，8，16……）后，之后的其实就是新的位数+之前的位数，Code里用两种方式求解，第二种看起来更简洁，实际上应该是一样的。  
