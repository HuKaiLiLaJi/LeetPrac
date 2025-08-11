from q1 import Sorts
from my_list import My_list
from my_list import Node

def main():

    print("Hello, this is the main program!")
    obj= Sorts()
    arr=[3,4,1,5,6,2,0,9,0]
    #print(obj.break_arr(arr))
    ll = My_list()
    ll.add_to_head(10)
    ll.add_to_head(20)
    ll.add_to_head(30)
    ll.add_to_head(50)
    
    ll.head = ll.reverse_list_digui(ll.head)

    print(ll.select_all())
    
  


















if __name__ == "__main__":
    # This ensures the code only runs when executed directly,
    # and not when imported as a module.
    main()
