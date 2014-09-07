from random import randint
def prot(a,row,col,s=0):
    ex=col-s
    ey=row-s
    for i in range(s,ex):
        print a[s][i]
    for j in range(s+1,ey):
        print a[j][ex-1]

    for k in range(ex-2,s-1,-1):
        print a[ey-1][k]

    for m in range(ey-2,s,-1):
        print a[m][s]

def pcur(a):
    r=len(a)
    c=len(a[0])
    st=0
    while r>0 and c>0:
        prot(a,r,c,st)
        r-=2
        c-=2
        st+=1

arr=[[randint(1,99) for i in range(6)] for j in range(4)]
for a in arr:
    print a
pcur(arr)
