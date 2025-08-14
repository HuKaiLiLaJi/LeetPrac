class Solution148:
    def sortList(self, head) :
        if head is None or head.next is None:
            return
        
        fast=head
        slow=head
        list1=head 
        list2=None
        while fast is not None and fast.next is not None:
            fast=fast.next.next 
            slow=slow.next 
        list2=slow.next 
        slow.next=None
        left=self.sortList(list1)
        right=self.sortList(list2)   
        
        return self.merge(left,right)
        
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