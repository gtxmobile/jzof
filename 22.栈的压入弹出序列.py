
from random import randint
def pushpop(a,b):
    j=0
    i=0
    ass=[]
    top=0
    while j<len(b):
        if ass and ass[-1]==b[j]:
            print "pop ",ass.pop()
            j+=1
        else:
            try:
                ass.append(a[i])
                print "push ",a[i]
                i+=1
            except:
                return False

    if i==j:
        return True
    else:
        return False

a=[randint(0,4) for i in range(5)]
b=[randint(0,4) for j in range(5)]
print a
print b
pushpop(a,b)
