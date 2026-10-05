class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        b=[]
        a=list(s)
        for i in a:
            if (i>='a' and i<='z') or (i>='A' and i<='Z') or (i >= '0' and i <= '9'):
                b+=i
                
        st="".join(map(str,b))
        ulta= str(st)[::-1]
        if st.upper()==ulta.upper():
            return True
        else:
            return False
                
        

s = input('enter your text: ')

p=Solution()

out=p.isPalindrome(s)
print(out)

        
     
        
