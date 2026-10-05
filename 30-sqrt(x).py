 class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        s=0
        e=x
        m=(s+e)//2
        
        while s<=e:
            if m*m==x:
                return m
            elif m*m>x:
                e=m-1
            else:
                s=m+1
            m=(s+e)//2
        return m            
                    
        
x=int(input('enter num: '))
ou=Solution()

out= ou.mySqrt(x)
print(out)        