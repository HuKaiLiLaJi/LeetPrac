class Solution141:
    def hasCycle(self, head) -> bool:
        fast=head
        slow=head
        
        while fast is not None and fast.next is not None:
            fast= fast.next.next 
            slow = slow.next 
            if fast == slow :
                return True
            
        return False
        
        
        
        