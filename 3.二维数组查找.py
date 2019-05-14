#encoding: utf-8

#二维数组查找
from random import randint
def find2d(a,x):
    rowlen=len(a[0])
    for i in range(rowlen-1,-1,-1):
        if a[0][i]<x:
            for j in range(len(a)):
                if a[j][i]==x:
                    return j,k
                elif a[j][i]>x:
                    for k in range(i,-1,-1):
                        if a[j][k]==x:
                            return j,k
                    return False
            return False
        elif a[i][x]==x:
            return i,0
    return False


arr=[[randint(i*100+j*10,i*100+(j+1)*10) for j in range(10)] for i in range(10)]

for i in range(10):
    print arr[i]

print(find2d(arr,arr[3][6]))



