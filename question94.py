class Solution94:
    
    def inorderTraversal(self, root) :
        
        res=[]
        sup_stack=[]
        current=root
        
        while current is not None or len(sup_stack) >0:
            if current is not None:
                
                
                sup_stack.append(current)
                current=current.left
            else:
                current=sup_stack.pop()
                res.append(current.val)
                current=current.right
        return res    