class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        x=0
        t=list(map(str,s))
        c=1
        if t[len(t)-c]==" ":
            
                c=self.increase(c,t)  
                
                for i in range(len(t)-(c+1),-1,-1):
                    if  t[i]==" ":
                     break
           
                    x+=1
                    
                               
        else:    
            
            for i in range(len(t)-1,-1,-1):
             if  t[i]==" ":
                break
           
             x+=1
        
        return x   
    
    def increase(self,c,t):
        if t[len(t)-(c+1)]!=" ":
            return c
        else :
            return self.increase(c+1,t)
      
                        
             
        
s = input('enter your line: ')   
a= Solution()
b=a.lengthOfLastWord(s)

print(b)


     