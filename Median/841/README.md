# 841.钥匙和房间
## 有 N 个房间，开始时你位于 0 号房间。每个房间有不同的号码：0，1，2，...，N-1，并且房间里可能有一些钥匙能使你进入下一个房间。  
在形式上，对于每个房间 i 都有一个钥匙列表 rooms[i]，每个钥匙 rooms[i][j] 由 [0,1，...，N-1] 中的一个整数表示，其中 N = rooms.length。 钥匙 rooms[i][j] = v 可以打开编号为 v 的房间。  
最初，除 0 号房间外的其余所有房间都被锁住。  
你可以自由地在房间之间来回走动。  
如果能进入每个房间返回 true，否则返回 false。  
## 示例 1：
* 输入: [[1],[2],[3],[]]  
输出: true  
解释:    
我们从 0 号房间开始，拿到钥匙 1。  
之后我们去 1 号房间，拿到钥匙 2。  
然后我们去 2 号房间，拿到钥匙 3。 
最后我们去了 3 号房间。  
由于我们能够进入每个房间，我们返回 true。  
## 示例 2：
* 输入：[[1,3],[3,0,1],[2],[0]]  
输出：false  
解释：我们不能进入 2 号房间。  
## 提示
* 1 <= rooms.length <= 1000
* 0 <= rooms[i].length <= 1000
* 所有房间中的钥匙数量总计不超过 3000。
## 解题思路
### BFS
* 在本题中，广度优先遍历是一种比较容易想到的方法。即读进一个房间内所有的钥匙，之后每pop一个钥匙再将新房间内的钥匙并到钥匙库中。本题中需要考虑的是在多个房间中可能存在相同的钥匙，需要使用Set或者在使用List时添加一层是否存在的判断，在算法实现的第一种方法里我使用了List并再  
判定是否有重复的方法，提交之后运行时间为124ms，耗时较大。
### DFS
* 本题中运用的也是常规的DFS方法，算法实现使用递归的方法，以深度优先进行遍历，耗时相对较少，在提交时的运行时间为76ms