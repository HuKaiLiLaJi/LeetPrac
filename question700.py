class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution700:
    def searchBST(self, root , val: int):
        if root is None:
            return None
        
        if root.val==val:
            return root
        elif root.val<val:
            root=root.right
            return self.searchBST(root,val)
        else:
            root=root.left
            return self.searchBST(root,val)