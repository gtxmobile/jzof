
def vsobst(a):
    root=a[-1]
    mid=0
    while a[mid]<root:
        mid+=1
    j=mid
    for k in range(mid,len(a)-1):
        if a[k]<root:
            return False
    lf=True
    if mid>0:
        lf=vsobst(a[0:mid])
    rf=True

    if mid<len(a)-1:rf=vsobst(a[mid:-1])
    return lf and rf
a=[5,7,6,9,11,10,8]
a=[7,4,6,5]
print vsobst(a)
