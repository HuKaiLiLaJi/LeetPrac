# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution144:
    def preorderTraversal(self, root: TreeNode) :
        res=[]
        if root is None:
            return res
        sup_stack=[]
        sup_stack.append(root)
        while len(sup_stack)>0:
            node=sup_stack.pop()
            res.append(node)
            if node.right is not None:
                sup_stack.append(root.right)
            if node.left:
                sup_stack.append(root.left)
        return res
        