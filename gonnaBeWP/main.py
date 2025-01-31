# https://www.acmicpc.net/problem/2775
T = int(input())
K=[] #층
N=[] #호

for i in range(0,T):
    K.append(int(input()))
    N.append(int(input()))
for i in range(0,T):
    k=K[i]
    n=N[i]
    outerArray=[]
    innerArray=[]
    for i in range(0,n):
        innerArray.append(i+1)
    outerArray.append(innerArray)
    for j in range(1,k+1):
        innerArray = []
        innerArray.append(1)
        for i in range(1,n):
            innerArray.append(innerArray[i-1]+outerArray[j-1][i])
        outerArray.append(innerArray)
    print(outerArray[k][n-1])