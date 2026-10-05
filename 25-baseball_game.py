class Solution(object):
    def calPoints(self, operations):
       
        a=[]
        s=len(a)
        for i in range(len(operations)):
            if operations[i] == '+':
                x=int(a[len(a)-1])+int(a[len(a)-2])
               
                a.append(x)
            elif  operations[i] == 'C': 
                a.pop()
            elif operations[i]=='D':
                z=2*int(a[len(a)-1])
                
                a.append(z) 
            else:
                a.append(int(operations[i]))     
        return sum(a)        
        
operations = list(map(str,input('enter your op: ').split()))        

out =Solution()
output =  out.calPoints(operations)
print(output)