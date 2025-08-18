class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution106:
    def buildTree(self, inorder: list[int], postorder: list[int]) :
        if len(inorder)==0:
            return None
        if len(inorder)==1:
            return TreeNode(val=inorder[0])
        
        length= len(postorder)
        root=TreeNode(val=postorder[length-1])
        
        mid=inorder.index(postorder[length-1])
        in_left=inorder[:mid]
        in_right=inorder[mid+1:]
        post_left=postorder[:mid]
        post_right=postorder[mid:len(postorder)-1]
        
        root.left=self.buildTree(in_left,post_left)
        root.right=self.buildTree(in_right,post_right)
        
        return root