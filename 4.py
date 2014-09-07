#encoding: utf-8

#二维数组查找
from random import randint

def replce20(s):
    cnt=0
    for i in s:
        if i==' ':
            cnt+=1
    rawlen=len(s)
    s+=(2*cnt*' ')
    s=list(s)
    for i in range(rawlen-1,-1,-1):
        if s[i]==' ':
            print i+cnt*2
            s[i+cnt*2]='0'
            s[i+cnt*2-1]='2'
            cnt-=1
            s[i+cnt*2]='%'
        else:
            s[i+cnt*2]=s[i]

    print s

replce20("fa f'awejf fjale fa faje")
