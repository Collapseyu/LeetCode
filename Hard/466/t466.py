class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        news1=""

        for i in s1:
            if i in s2:
                news1+=i
        for j in s2:
            flag=0
            for i in news1:
                if i==j:
                    flag=1
                    break
            if flag==0:
                return 0

        s1Count=0
        s2Count=0
        s1ptr=0
        s2ptr=0
      
        exitFlag=0
        hitList=[]
        totalCount=0
        while(1):
            
            if news1[s1ptr]==s2[s2ptr]:
                s1ptr+=1
                s2ptr+=1
                exitFlag=0
            else:
                s1ptr+=1
            totalCount+=1
            if totalCount==n1*len(news1):
                break
            if s1ptr==len(news1):
                s1ptr=0
                s1Count+=1
                if exitFlag:
                    break
            if s2ptr==len(s2):
                s2Count+=1
                if s1ptr==0:
                    hitList.append(s1Count)
                    break
                hitList.append(s1Count+1)
                s2ptr=0
                exitFlag=1
        
        res=(n1//s1Count)*s2Count
        res=res//n2
        other=n1%s1Count
        for i in range(len(hitList)):
            if hitList[i]>other:
                res+=i
                break
        return res
    def getMaxRepetitions_1(self, s1: str, n1: int, s2: str, n2: int) -> int:
        news1=""
        if n1==0:
            return 0
        for i in s1:
            if i in s2:
                news1+=i
        for j in s2:
            flag=0
            for i in news1:
                if i==j:
                    flag=1
                    break
            if flag==0:
                return 0
        longth=1
        orinews1=news1
        if len(news1)<len(s2):
            longth=len(s2)//len(news1)+1
            news1=news1*(longth)
            print(news1)
            print('long',longth)
        status=0
        hitFlag=0
        limit=len(news1)//len(s2)
        s2N=0
        hitStep=[]
        inflag=0
        for i in range(1,limit+1):
            successFlag=0
            hitStep=[]
            s1Count=0
            s2Count=0
            s1ptr=0
            s2ptr=0
            news2=s2*i
            totalStep=0
            while(1):
                if s2Count==3:
                    if (hitStep[-1]-hitStep[-2])==(hitStep[-2]-hitStep[-3]):
                        successFlag=1
                    else:
                        successFlag=0
                    break
                if news1[s1ptr]==news2[s2ptr]:
                    s1ptr+=1
                    s2ptr+=1
                else:
                    s1ptr+=1
                totalStep+=1

                if s1ptr==len(news1):
                    s1ptr=0
                    s1Count+=1
                
                if s2ptr==len(news2):
                    s2ptr=0
                    hitStep.append(totalStep)
                    s2Count+=1
                    if (s1Count==0 and s2Count==2):
                        successFlag=0
                        break
           
            if successFlag==1:
                s2N=i
                break
        print(hitStep)
        print(s2N)
        print(news1)
        print(news2)
        everyStep=hitStep[-1]-hitStep[-2]
        startStep=hitStep[0]-everyStep
        print(len(news1))
        totalS1=len(news1)*n1//longth-startStep
        print(totalS1)
        totalS1//=everyStep
        s1ptr=totalS1*everyStep+startStep
        print(totalS1)
        totalS1*=s2N
        print(totalS1)
        res=totalS1//n2
        
        print(s1ptr)
        news1=orinews1*n1
        print(len(news1))
        print(news1[s1ptr:])
        s2ptr=0
        while(s1ptr<len(news1)):
            if news1[s1ptr]==news2[s2ptr]:
                    s1ptr+=1
                    s2ptr+=1
            else:
                    s1ptr+=1
            if s2ptr==len(news2):
                res+=1
                s2ptr=0
                    
        return res

        

        

        

        
        