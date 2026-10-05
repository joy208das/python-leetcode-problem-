class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a=int("".join(map(str,digits)))
        b=a+1
        c= list(map(int,str(b)))
        return c
        

digits= list(map(int,input('enter elements:').split()))    

p= Solution()

x=p.plusOne(digits)

print(x)    


        
