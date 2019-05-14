#-*- coding: utf-8 -*-

def printn(n):
    if n<0:
        return
    num=[0]*n
    for i in range(10):
        num[0]=str(i)
        printrec(num)

def printrec(num,idx=0):
    if idx==len(num)-1:
        print(''.join(num))
        return
    for i in range(10):
        num[idx+1]=str(i)
        printrec(num,idx+1)


printn(4)
