# https://www.acmicpc.net/problem/10250
a = []
for i in range(0,int(input())):
    a.append(input())
for j in a:
    H,W,N = map(int,j.split(' '))
    w=int(N/H)
    h=H
    if N%H!=0:
        w = int(N / H)+1
        h = int(N % H)
    if w >= 10:
        print(str(h) + str(w))
    else:
        print(str(h) +"0"+ str(w))
