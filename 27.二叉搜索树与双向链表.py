#encofing: utf-8

class TreeNode:
    def __init__(self
def tree2dl(r,lst):
    if not r:
        return
    if not r.left:
        tree2dl(r.left,lst)
    r.left=lst
    if not lst:
        lst.right=r
    lst=r
    if not r.right:
        tree2dl(r.right,lst)

def convert(r):
    lst=None
    tree2dl
