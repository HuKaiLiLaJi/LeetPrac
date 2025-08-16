from q1 import Sorts
from my_list import My_list
from my_list import Node
from question2 import Solution2
from question20 import Solution20
from question3 import Solution3
from question209 import Solution209
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class MyLinkedList:
    def __init__(self):
        self.head = None

    # 添加到链表末尾
    def add(self, val):
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        cur = self.head
        while cur.next:  # 找到最后一个节点
            cur = cur.next
        cur.next = new_node

    # 打印链表
    def display(self):
        cur = self.head
        while cur:
            print(cur.val, end=" -> ")
            cur = cur.next
        print("None")



def print_list(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next
    print("None")


def main():

    print("Hello, this is the main program!")
    obj= Solution209()
    
    print(obj.minSubArrayLen(7,[2,3,1,2,4,3]))
  


















if __name__ == "__main__":
    # This ensures the code only runs when executed directly,
    # and not when imported as a module.
    main()
