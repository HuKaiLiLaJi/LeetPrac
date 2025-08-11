

class Sorts():
    def bubble(self,arr):
        for i in range (0,len(arr)-1):
            for j in range (0,len(arr)-i-1):
                if(arr[j]>arr[j+1]):
                    a=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=a
        return arr
    
    def quick(self,arr):
        n= len(arr)
        if(n<=1):
            return arr
        pivot= arr[0]
        left=[]
        right=[]
        eq=[]
        eq.append(pivot)
        for i in range(1,n):
            if arr[i]>pivot:
                right.append(arr[i])
            if arr[i]<pivot:
                left.append(arr[i])
            if arr[i]==pivot:
                eq.append(arr[i])
        
        return self.quick(left)+eq+self.quick(right)
    
    
    
    def break_arr(self,arr):
        if len(arr)<=1:
            return arr
        
        mid = len(arr)//2
        left= self.break_arr(arr[:mid])
        right= self.break_arr(arr[mid:])
        
        
        return self.merge_arr(left,right)
            
    
    def merge_arr(self,left,right):
        res=[]   
        i=0
        j=0
        while(i<len(left)and j<len(right)):
            if left[i]<=right[j]:
                res.append(left[i])
                i=i+1
            else:
                res.append(right[j])
                j=j+1
        
        res.extend(left[i:])  
        res.extend(right[j:])  
        
        return res
        
        
        
        
        
        
        
        
        
        
        
        
        
        