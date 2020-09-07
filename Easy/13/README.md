# 罗马数字转整数
## 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。  
&ensp;字符          &ensp;数值    
&ensp;I            &ensp;&ensp;&ensp;&ensp;1    
&ensp;V            &ensp;&ensp;&ensp;5  
&ensp;X             &ensp;&ensp;&ensp;10  
&ensp;L             &ensp;&ensp;&ensp;50  
&ensp;C             &ensp;&ensp;&ensp;100  
&ensp;D             &ensp;&ensp;&ensp;500  
&ensp;M             &ensp;&ensp;&ensp;1000  
例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。  
通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。  
这个特殊的规则只适用于以下六种情况：  
I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。  
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。   
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。  
给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。  
## 示例
### 一
&ensp;输入: "III"  
&ensp;输出: 3
### 二
&ensp;输入:"IV"  
&ensp;输出:4
## 解题思路
* 先把一个罗马字符和两个罗马字符分别存放到字典里
* 扫描字符串，先用两个去找，找不到再回来找一个的匹配。（需要注意的是，在python for i in range(N) 中，在循环中改变i的值并不会确实改变）
