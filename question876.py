class Solution876:
    def middleNode(self, head) :
        
        fast= head 
        slow= head
        
        if head.next is None :
            return head
        if head.next.next is None:
            return head.next
        
        while fast is not None and fast.next is not None:
            fast=fast.next.next 
            slow= slow.next    
        return slow  
        
    
        