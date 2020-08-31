from typing import List
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        roomsCount=len(rooms)
        checkRoom=[0]*roomsCount
        roomKeys=[]
        alreadyInRoom=[]
        nowPlace=0
        while(len(alreadyInRoom)<roomsCount-1):
            
            newKeys=list(set(rooms[nowPlace]).difference(set(alreadyInRoom)))
            roomKeys=list(set(roomKeys).union(set(newKeys)))
            if len(roomKeys)==0:
                break
            tmpKey=roomKeys.pop(0)
            nowPlace=tmpKey
            alreadyInRoom.append(tmpKey)
        print(alreadyInRoom)
        if 0 in alreadyInRoom:
            trueCount=roomsCount-2
        else:
            trueCount=roomsCount-1
        if len(alreadyInRoom)==trueCount:
            return True
        else:
            return False
    def canVisitAllRooms_dfs(self, rooms: List[List[int]]) -> bool:
        def dfs(x: int):
            vis.add(x)
            nonlocal num 
            num += 1 
            for it in rooms[x]:
                if it not in vis:
                    dfs(it)
        num=0
        vis=set()
        dfs(0)
        return num==len(rooms)