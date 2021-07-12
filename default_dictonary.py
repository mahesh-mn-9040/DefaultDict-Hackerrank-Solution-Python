#defrault dictonary hacker4rank
from collections import defaultdict
n, m=map(int,input().split())
d=defaultdict(list)
li=[]
for i in range(1,n+1):#############starting with index 1
    d[input()].append(i)######################[a:1,2,4],[b:3,5]
#print(d)    
for j in range(m):
    li.append(input())###################[a,b]
for k in li:
    if k in d.keys():
        print(*d[k])  ##################for formatiing
    else:
        print(-1)