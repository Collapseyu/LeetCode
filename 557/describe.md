# 题目描述
## 反转字符串中的单词 III
* 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
* 示例：  
  输入："Let's take LeetCode contest"  
  输出："s'teL ekat edoCteeL tsetnoc"  
## 解题思路
### reverseWord
* 1、利用split将字符串依据空格切分，成为顺序排列的单词串  
  2、遍历所有单词，将每个单词倒序添加到结果中，并添加空格  
  3、考虑最后一个单词后不用添加空格
### reverseWord
* 1、s[::-1]将整个字符串倒序  
  2、s.split()按照空格进行切分  
  3、s.reverse()将list中的每一个单词倒置
  4、通过' '.join将list转换为string

