class Solution19:
    def removeNthFromEnd(self, head, n: int) :
        
        if head.next is None:
            return None
        
        fast=head
        slow = head
        for i in range(0,n):
            fast=fast.next
        while fast.next is not None:
            slow=slow.next
            fast=fast.next
        slow.next=slow.next.next
        
        
        return head
    
