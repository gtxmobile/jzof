
def top2bot(r):
    if not r:
        return
    a=[]
    while a:
        if r.left:
            a.append(r.left)
        if r.right:
            a.append(r.right)
        print a.pop(0).data

