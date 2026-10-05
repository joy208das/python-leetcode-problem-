class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a= l1[::-1]
        b = l2[::-1]
        
        a1 = int(''.join(map(str,a)))
        b2 = int(''.join(map(str,b)))
        
        c = a1 + b2
        
        main = list(map(int,str(c)))
        return main[::-1]
        
        
l1 = list(map(int, input().split())) 
l2 = list(map(int, input().split()))

ob= Solution()

ans = ob.addTwoNumbers(l1,l2)

print(ans)