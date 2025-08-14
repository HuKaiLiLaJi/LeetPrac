class Solution142:
    def detectCycle(self, head) :
        fast=head
        slow = head
        slow2=head
        i=0
        while fast is not None and fast.next is not None:
            fast=fast.next.next 
            slow=slow.next 
            if fast==slow:
                while True:
                    if slow2==slow:
                        return slow
                    slow=slow.next 
                    slow2=slow2.next 
                    
                    
        return head
    
    