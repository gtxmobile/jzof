from random import randint
def oddbeven(a):
    head=0
    for i in range(len(a)):
        if a[i] & 0x01==1:
            tmp=a[head]
            a[head]=a[i]
            a[i]=tmp
            head+=1
    print a

arr=[randint(1,100) for i in range(30)]
print arr
oddbeven(arr)

