class Solution101:
    def isSymmetric(self, root) :
        if root is None:
            return True
        return self.check(root.left,root.right)
    
    
    def check(self,left,right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False     
        if left.val != right.val :
            return False
        
        return self.check(left.left,right.right) and self.check(left.right,right.left)