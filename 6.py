#encoding: utf-8

#二维数组查找
from random import randint

def restoreBinTree(preorder,inorder):
    for i in range(len(inorder)):
        if preorder[0]==inorder[i]:
            r=treeNode(preorder[0])
            r.l=restoreBinTree(preorder[1:i],inorder[0:i-1])
            r.r=restoreBinTree(preorder[i+1::],inorder[i+1::])
