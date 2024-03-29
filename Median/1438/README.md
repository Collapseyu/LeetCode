# 绝对差不超过限制的最长连续子数组
## 给你一个整数数组 nums ，和一个表示限制的整数 limit，请你返回最长连续子数组的长度，该子数组中的任意两个元素之间的绝对差必须小于或者等于 limit 。如果不存在满足条件的子数组，则返回 0 。
## 示例  
### 输入：nums = [8,2,4,7], limit = 4  
输出：2   
解释：所有子数组如下：  
[8] 最大绝对差 |8-8| = 0 <= 4.  
[8,2] 最大绝对差 |8-2| = 6 > 4.   
[8,2,4] 最大绝对差 |8-2| = 6 > 4.  
[8,2,4,7] 最大绝对差 |8-2| = 6 > 4.  
[2] 最大绝对差 |2-2| = 0 <= 4.  
[2,4] 最大绝对差 |2-4| = 2 <= 4.  
[2,4,7] 最大绝对差 |2-7| = 5 > 4.  
[4] 最大绝对差 |4-4| = 0 <= 4.  
[4,7] 最大绝对差 |4-7| = 3 <= 4.  
[7] 最大绝对差 |7-7| = 0 <= 4.   
因此，满足题意的最长子数组的长度为 2。  
### 输入：nums = [10,1,2,4,7,2], limit = 5  
输出：4   
解释：满足题意的最长子数组是 [2,4,7,2]，其最大绝对差 |2-7| = 5 <= 5 。  
### 输入：nums = [4,2,2,2,4,4,2,2], limit = 0  
输出：3  
## 解题思路
### STEP 1  
这回吸取教训了，拿到题之后感觉这题是一道滑动窗口题，和之前的连续1这种题的差别在于需要维护一下窗口内的大小顺序。具体思路类似，也是通过不断扩大滑动窗口的窗口值求解。
所以在第一种做法里使用了双指针滑做滑动窗口，同时用了额外空间维护了窗口内的顺序，第一种解法想要简单一些，所以只是用了插入法做排序，总体时间复杂度为O(N^2)，提交结果显示
超时
### STEP 2  
第二种解法和第一种解法实际上是一脉相传的，只是在维护顺序的时候用了二分法查找，这样可以把维护排序顺序的时间复杂度降低为O(NLogN)。提交成功
### STEP 3   
第三种做法是看了题解之后的使用双端序列维护大小顺序的方法。主要想法是维护两个双端序列（双端序列指的是能同时从序列的头部和尾部进行操作的序列）。在这种做法里使用了两个
序列，第一个序列维护一个递减序列表示最大值，第二个序列维护一个递增序列表示最小值。刚开始看到这种方法的时候想不明白的点是：当新的值加入到这两个序列过程中，可能会使得之前
的第二大或者第三大（第二小或第三小）的数直接消失，不再记录，这样当左指针开始移动时，就无法有效的表示该窗口内的最大值和最小值了。  
但实际上，会把这些数冲掉的新数字只会是新的第二大（第二小）的数，由于滑动窗口的特性，右指针滑到的值是更为重要的值，因为当条件不成立滑动左指针时，如果最右边的值是第二大
（第二小）的情况，那么在这个值之前的第三小，第三大的值实际上是没有用的，所以这些值是没有必要去进行记录的。解决了这一点疑惑之后，后续的问题就引刃而解了。
