class Solution100:
    def isSameTree(self, p, q) -> bool:
        if p is not None and q is not None:
            return True
        if p is not None or q is not None:
            return False
        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        