class MinStack:

    def __init__(self):
        self.my_stack=[]
        self.sup_stack=[]
        self.min_val=2147483647
        
        

    def push(self, val: int) -> None:
        
        self.my_stack.append(val)
        if not self.sup_stack or val< self.sup_stack[-1]:
            self.sup_stack.append(val)
        else:
            self.sup_stack.append(self.sup_stack[-1])
        
        
        
    def pop(self) -> None:
        x=self.my_stack[len(self.my_stack)-1]
        self.my_stack.pop()
        self.sup_stack.pop()
        return x

    def top(self) -> int:
        return self.my_stack[-1]

    def getMin(self) -> int:
        return self.sup_stack[-1]