class MyQueue:

    def __init__(self):
        self.main_stack=[]
        self.sup_stack=[]
        
    def push(self, x: int) -> None:
        self.sup_stack.append(x)
        
        

    def pop(self) -> int:
        if len(self.main_stack)>0:
            return self.main_stack.pop()
        
        while len(self.sup_stack)>0 and len(self.main_stack)==0:
            self.main_stack.append(self.sup_stack.pop())
        return self.main_stack.pop()
        

    def peek(self) -> int:
        if len(self.main_stack)>0:
            return self.main_stack[len(self.main_stack)-1]
        
        while len(self.sup_stack)>0 and len(self.main_stack)==0:
            self.main_stack.append(self.sup_stack.pop())
        return self.main_stack[len(self.main_stack)-1]
        

    def empty(self) -> bool:
        while len(self.sup_stack)>0:
            self.main_stack.append(self.sup_stack.pop())
        if len(self.main_stack   )>0:
            return False
        else :
            return True 
        