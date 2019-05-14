#encoding: utf-8

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
#重建二叉树
def restoreBinTree(preorder,inorder):
    for i in range(len(inorder)):
        if preorder[0]==inorder[i]:
            r=TreeNode(preorder[0])
            r.l=restoreBinTree(preorder[1:i],inorder[0:i-1])
            r.r=restoreBinTree(preorder[i+1::],inorder[i+1::])
