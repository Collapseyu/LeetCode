# 至少有 K 个重复字符的最长子串
## 题目描述  
###    
给你一个字符串 s 和一个整数 k ，请你找出 s 中的最长子串， 要求该子串中的每一字符出现次数都不少于 k 。返回这一子串的长度。
## 示例
### 1  
输入：s = "aaabb", k = 3
输出：3
解释：最长子串为 "aaa" ，其中 'a' 重复了 3 次。
### 2  
输入：s = "ababbc", k = 2
输出：5
解释：最长子串为 "ababb" ，其中 'a' 重复了 2 次， 'b' 重复了 3 次。
## 解题思路
### STEP 1：
其实拿到题之后想用滑动窗口做的，但这道题常规的滑动窗口没法解决（看了题解之后才发现可以用另一种方法来做，不过感觉确实很难想到），走了点弯路之后觉得这就是道递归题，用异常值把序列切开送到函数里，继续切
，直到送进去的序列满足要求。为了实现这个功能，我写了两部分的函数，第一部分是找出异常值点（顺便可以判断序列是不是符合要求），具体做法是用一个哈希表存下序列中每一种字符出现的次数及索引，返回值就是这些
索引的List（为了使后续方便切分序列，返回前我将索引序列排了下序）。另一个函数就是递归的主题函数，主要想法就是找异常点，判断，切分，递归，如此如此。
### STEP 2：  
第二种做法是看了题解之后的滑动窗口做法（不过我觉得这种滑动窗口的做法没有那么巧妙）。由于题目中限制了只会出现小写字母，所以算法通过规定窗口中可能出现的字符种类数来滑动。具体的，在算法执行（滑动）过程
中，首先要确保的是窗口中的字符串种类数，其次是要保证各个字符的出现次数。再在每次符合规定的序列出现时记录一下长度，并和最大值对比，决定是否替换最大值。