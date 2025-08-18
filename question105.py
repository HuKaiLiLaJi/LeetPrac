class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution105:
    def buildTree(self, preorder: list[int], inorder: list[int]) :
        if len(preorder)==0:
            return None
        
        if len(preorder)==1:
            return TreeNode(val=preorder[0])
        
        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])
        
        
        in_left=inorder[:mid]
        in_right=inorder[mid+1:]
        pre_left=preorder[1:mid+1]
        pre_right=preorder[mid+1:]
        
        root.left=self.buildTree(pre_left,in_left)
        root.right=self.buildTree(pre_right,in_right)
        
        return root