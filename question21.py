class Solution21:
    def mergeTwoLists(self, list1, list2) :
        cur1=list1
        cur2=list2
        new_head=ListNode(None)
        support=new_head
        while cur1 is not None and cur2 is not None:
            if cur1.val<=cur2.val:
                new_head.next=cur1
                cur1=cur1.next 
            else:
                new_head.next=cur2
                cur2=cur2.next
            new_head=new_head.next
        new_head.next=cur1 or cur2
        
        
                
                
        
        return support.next