class Node():
    def __init__(self,data):
        self.data= data
        self.next =None
        
        
class My_list():
    def __init__(self):
        self.head= None
        
    def select_all(self):
        current = self.head
        while current is not None :
            print(current.data)
            current=current.next    
        
        
    def add_to_last(self,data):
        if self.head is None:
            self.head=Node(data)
            return
        
        
        currtent= self.head
        while currtent.next is not None:
            currtent=currtent.next
        currtent.next=Node(data)
    
    def add_to_head(self,data):
        if self.head is None:
            self.head=Node(data)
            return   
        current=Node(data)
        current.next=self.head
        self.head=current
        
    def get_len(self):
        current= self.head
        i=0
        while current is not None:
            current=current.next
            i=i+1
        return i
    
    def reverse_list_diedai(self):
        current = self.head
        prev=None
        if current is None or current.next is None:
            return 
        while current is not None:
            helper=current.next
            current.next=prev
            prev=current
            current=helper
            
        self.head=prev
        
    def reverse_list_digui(self,node):
        
        if node is None:
            return None
        
        if node.next is None:
            return node
        helper=self.reverse_list_digui(node.next)
        node.next.next=node
        node.next=None
        return helper
            