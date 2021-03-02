from typing import List
def digitsum(n):
    ans = 0
    while n:
        ans += n % 10
        n //= 10
    return ans

class Solution:
    def judge_method(self,x,y,k):
        res = 0
        while(x > 0):
            res += x%10
            x //= 10
        while(y > 0):
            res += y%10
            y //= 10
        if res > k:
            return False
        else:
            return True
    def movingCount(self, m: int, n: int, k: int) -> int:
        from queue import Queue
        q = Queue()
        q.put((0, 0))
        s = set()
        while not q.empty():
            x, y = q.get()
            if (x, y) not in s and 0 <= x < m and 0 <= y < n and digitsum(x) + digitsum(y) <= k:
                s.add((x, y))
                for nx, ny in [(x + 1, y), (x, y + 1)]:
                    q.put((nx, ny))
        return len(s)
    def movingCount_bfs(self, m: int, n: int, k: int) -> int:
        matrix_flag = [[True for _ in range(n)] for _ in range(m)]
        node_queue = []
        res = 0
        node_queue.append([0,0])
        matrix_flag[0][0] = False
        while(len(node_queue) != 0):
            current_node = node_queue[0]
            # print(current_node)
            del node_queue[0]
            res += 1 
            if current_node[0] + 1 < m and matrix_flag[current_node[0]+1][current_node[1]] and self.judge_method(current_node[0]+1,current_node[1],k):
                node_queue.append([current_node[0]+1,current_node[1]])
                matrix_flag[current_node[0]+1][current_node[1]] = False
            if current_node[1] + 1 < n and matrix_flag[current_node[0]][current_node[1] + 1] and self.judge_method(current_node[0],current_node[1]+1,k):
                node_queue.append([current_node[0],current_node[1]+1])
                matrix_flag[current_node[0]][current_node[1]+1] = False
        return res
    def dfs(self,x,y,m,n,k,flag):
        if not (0 <= x < m) or not(0 <= y < n) or not self.judge_method(x,y,k) or not flag[x][y]:
            return 0,flag
        flag[x][y] = False
        tmp_x,flag = self.dfs(x+1,y,m,n,k,flag)
        tmp_y,flag = self.dfs(x,y+1,m,n,k,flag)
        return 1 + tmp_x + tmp_y,flag

    def movingCount_dfs(self, m: int, n: int, k: int) -> int:
        matrix_flag = [[True for _ in range(n)] for _ in range(m)]
        return self.dfs(0,0,m,n,k,matrix_flag)[0]