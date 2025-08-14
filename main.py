from q1 import Sorts
from my_list import My_list
from my_list import Node
from question2 import Solution2


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
    obj= Solution2()
    arr=[3,4,1,5,6,2,0,9,0]
    #print(obj.break_arr(arr))
    l1=MyLinkedList()
    l1.add(1)
    l1.add(1)
    l1.add(1)
    l1.add(3)
    l1.add(9)
    l2=MyLinkedList()
    l2.add(6)
    l2.add(8)
    l2.add(4)
    l2.add(9)
    print_list(obj.addTwoNumbers(l1.head,l2.head))
  


















if __name__ == "__main__":
    # This ensures the code only runs when executed directly,
    # and not when imported as a module.
    main()
