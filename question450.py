class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deleteNode(self, root, key: int) :
        if root is None:
            return
        
        if root.val==key:
            if root.left is None and root.right is not None:
                return root.right
            if root.left is not None and root.right is None:
                return root.left
            if root.left and root.right:
                min_node= root.right
                while min_node.left :
                    min_node=min_node.left
                root.val=min_node.val
                root.right = self.deleteNode(root.right, min_node.val)
            if root.left is None and root.right is None:
                return None
        
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        else:
            root.right=self.deleteNode(root.right,key)
        
        return root
        
        pass