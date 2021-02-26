# 猜字谜
## 题目描述
###  
外国友人仿照中国字谜设计了一个英文版猜字谜小游戏，请你来猜猜看吧。  
字谜的迷面 puzzle 按字符串形式给出，如果一个单词 word 符合下面两个条件，那么它就可以算作谜底：  
&emsp;&emsp; 1)单词 word 中包含谜面 puzzle 的第一个字母。  
&emsp;&emsp; 2)单词 word 中的每一个字母都可以在谜面 puzzle 中找到。  
例如，如果字谜的谜面是 "abcdefg"，那么可以作为谜底的单词有 "faced", "cabbage", 和 "baggage"；而 "beefed"（不含字母 "a"）以及 "based"（其中的 "s" 没有出现在谜面中）。
返回一个答案数组 answer，数组中的每个元素 answer[i] 是在给出的单词列表 words 中可以作为字谜迷面 puzzles[i] 所对应的谜底的单词数目  
## 示例
### 1
#### 输入：
words = ["aaaa","asas","able","ability","actt","actor","access"],   
puzzles = ["aboveyz","abrodyz","abslute","absoryz","actresz","gaswxyz"]  
输出：[1,1,3,2,4,0]  
#### 解释：
1 个单词可以作为 "aboveyz" 的谜底 : "aaaa"   
1 个单词可以作为 "abrodyz" 的谜底 : "aaaa"  
3 个单词可以作为 "abslute" 的谜底 : "aaaa", "asas", "able"  
2 个单词可以作为 "absoryz" 的谜底 : "aaaa", "asas"  
4 个单词可以作为 "actresz" 的谜底 : "aaaa", "asas", "actt", "access"  
没有单词可以作为 "gaswxyz" 的谜底，因为列表中的单词都不含字母 'g'。  
## 解题思路
### STEP1：  
拿到题目之后的第一个想法是用两种hash表将谜底和谜面表示出来，之后再去遍历统计答案即可，开始用的hash是用python的dict表示，结果超时
### STEP2:  
第一次改进的思路是把dict结构改成二进制数，题目在后面有说都是小写字母。所以每一个puzzle可以用一个26位的二进制数表示，进行简单的位操作会达到加速效果，但仍然超时
### STEP3:
参考题解，题解的思路是把word的二进制串存到一个hash表里，想到与用这个二进制串作为唯一标示（即key），而value是该key在所有word里出现的次数。之后对puzzle的操作是找出puzzle二进制表示的所有子串，
有个操作还蛮有意思的之前没见过，主要是用来获得子串的：  
&emsp;&emsp;subset=mask  
&emsp;&emsp;while subset:  
&emsp;&emsp;&emsp;subset&ensp;=&ensp;(subset-1)&mask
&esmp;&emsp;将subset加入到子串列表  
这边的与操作保证了子串里的1位是原串中就有的1位。这样获得的子串呢去字典里查询一次就可以得到在words中出现的次数了
