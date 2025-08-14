class MyStack:

    def __init__(self):
        self.que1=[]
        self.que2=[]
        
        

    def push(self, x: int) -> None:
        self.que1.append(x)
        
        

    def pop(self) -> int:
        if len(self.que1)==1:
            return self.que1.pop(0)
        
        for i in range(0,len(self.que1)-1):
            self.que2.append(self.que1.pop(0))
        res = self.que1.pop(0)
        for i in range(0,len(self.que2)):
            self.que1.append(self.que2.pop(0))    
        return res
        

    def top(self) -> int:
         
        return self.que1[len(self.que1)-1]
        

    def empty(self) -> bool:
        if(len(self.que1)>0):
            return False
        else:
            return True