class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution2:
    def addTwoNumbers(self, l1 , l2 ):
        
        #if l1.next is not None:
        #  l1=self.rev_list(l1)
        
        #if l2.next is not None:
        #  l2=self.rev_list(l2)
        
        cur_l1=l1
        cur_l2=l2
        if self.search_all(l1)>=self.search_all(l2):
            head1=l1
            for i in range (0,self.search_all(l2)):
                cur_l1.val=cur_l1.val+cur_l2.val
                cur_l1=cur_l1.next 
                cur_l2=cur_l2.next 
            while l1 is not None:
                if l1.val>9:
                    l1.val=l1.val-10
                    if l1.next is not None:
                        l1.next.val=l1.next.val+1
                    else:
                        l1.next=ListNode(val=1,next=None)
                l1=l1.next
            return head1
        else:
            head2=l2
            for i in range (0,self.search_all(l1)):
                cur_l2.val=cur_l2.val+cur_l1.val
                cur_l1=cur_l1.next 
                cur_l2=cur_l2.next 
            while l2 is not None:
                if l2.val>9:
                    l2.val=l2.val-10
                    if l2.next is not None:
                        l2.next.val=l2.next.val+1
                    else:
                        l2.next=ListNode(val=1,next=None)
                l2=l2.next
            return head2
    
     
    
    def search_all(self,head):
        current=head
        i=0
        while current is not None:
            i=i+1
            current=current.next
        return i      
    
    def rev_list(self,head):
        if head is None or head.next is None:
            return 
        current= head
        prev= None
        while current is not None:
            helper=current.next
            current.next=prev
            prev=current
            current=helper
            
        return prev        