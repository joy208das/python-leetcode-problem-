class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        c=self.decimal(a)
        d=self.decimal(b)
        e=c+d
        y= self.trans(e)
        return str(y)
        
    def trans(self,e):
        binary=""
        
        if e==0:
            return 0
        while e>0:
            binary= str(e%2)+binary
            e=e//2
            
        return binary 
                
    def decimal(self,p):
        dec=0
        t=len(p)
        
        for i in range(t):
            bit = int(p[i])
            dec+=bit*(2**(t-1-i))
        return dec
        
                
a=input("enter 1st number:")
b=input('enter 2nd number: ') 
p= Solution()

x=p.addBinary(a,b)
print(x)