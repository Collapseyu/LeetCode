# 最大连续1的个数 III
## 给定一个由若干 0 和 1 组成的数组 A，我们最多可以将 K 个值从 0 变成 1 。  
返回仅包含 1 的最长（连续）子数组的长度。  
## 示例：  
1  
输入：A = [1,1,1,0,0,0,1,1,1,1,0], K = 2  
输出：6  
解释：   
[1,1,1,0,0,1,1,1,1,1,1]  
粗体数字从 0 翻转到 1，最长的子数组长度为 6。  
2    
输入：A = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3  
输出：10  
解释：   
[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]  
粗体数字从 0 翻转到 1，最长的子数组长度为 10。  
## 解题思路
Step 1 :   
虽然二月初做了很多的滑动窗口题，但碰到这道题的第一时间并没有想到要用滑动窗口做。大概是第一影响里计算每一位是个比较耗时的操作，所以第一种解法中，我想把数组中的1和0统计出来，这样在计算合并  
的时候会简化计算。但实际上计算统计值之后反而无法优化合并时候的算法，这导致了在统计数组里做合并的时间复杂度达到了O(N^2)这里的N指的是合并之后的数组长度。因为在这一步计算中，我用了遍历列举的方法进行  
最大值求解。当然，这种方法步骤复杂且耗时很久，提交后超时。  
Step 2 ：  
第二种做法使用了滑动窗口。实际上我对滑动窗口的理解还有一些问题，在第二种方法的滑动窗口中，我将窗口定义为遍历下的每一种情况，即每当右指针移动时我都会去判读一次当前是否是最大值的情况。在这  
一步上实际上花费了很多多余的时间。  
Step 3 ：   
第三种做法也是滑动窗口，但这是一种简化版的滑动窗口。在这种算法中，窗口是一个不断扩大的状态，具体来说，当我们发现tmpK的值小于K或者右指针指向的值为1的时候，意味着我们可以扩大我们的窗口。而  
当tmpK值大于K时，意味着无法继续扩大窗口，我们需要在维持这个窗口大小的情况下继续滑行来寻找扩大窗口的机会。在这个过程中就需要处理左指针的状态，主要是考虑左指针指向0的情况。
