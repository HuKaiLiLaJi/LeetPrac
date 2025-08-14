class Solution20:
    def isValid(self, s: str) -> bool:
        stack=[]
        my_map={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for i in range(0,len(s)):
            if s[i] in ['(','[','{']:
                stack.append(s[i])
            
            if s[i] in [')',']','}']:
                if len(stack)>0:
                    if my_map[s[i]]==stack.pop():
                        continue
                    else:
                        return False
                else:
                    return False   
        if len(stack)!=0:
            return False
        return True 
                    
                    
                
                
                
        