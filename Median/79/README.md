# 单词搜索
## 题目描述
*给定一个二维网格和一个单词，找出该单词是否存在于网格中。  
单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
## 示例：
* board =  
[  
  ['A','B','C','E'],  
  ['S','F','C','S'],  
  ['A','D','E','E']  
]  
* word="ABCCED",返回true
* word="SEE",返回true
* word=“ABCB”,返回false

## 解题思路
* 递归方法吧还是，定义一个是否去过的0，1矩阵，然后要现在整个矩阵里找到头字母，然后进入递归，每个字母可以走上下左右四个方向，判断一下边界值。  
* 值得注意的是，递归过程中会需要对每一个方向走一下，但其实在一个方向走通之后后续的方向是没有必要走的，为了节省时间（当然因为全跑一遍超时了），每个分支走完以后都判断一下是否是True，如果是就直接返回  
  这样时间144ms python3下的时间还可
