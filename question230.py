class Solution230:
    def kthSmallest(self, root, k: int) :
        
        in_order=self.in_order2(root)
        return in_order[k-1]
        
        
    
    
    
    def in_order(self,root)    :
        if root is None:
            return []
        return self.in_order(root.left)+[root.val]+self.in_order(root.right)
        
    def in_order2(self,root):
        
        res=[]
        sup_stack=[]
        current=root
        while sup_stack or current is not None:
            if current is not None:
                sup_stack.append(current)
                current=current.left
            else:
                current=sup_stack.pop()
                res.append(current.val)
                current=current.right
        return res    