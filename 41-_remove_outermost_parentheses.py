class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = [] 
        cn = 0 

        for i in s:
            if i == '(':
                if cn > 0:
                    result.append(i)
                cn += 1
            elif i == ')':
                cn -= 1
                if cn > 0:
                    result.append(i)  

        return ''.join(result)

        
s = input('enter your parentheses operations: ')

ou=Solution()
out = ou.removeOuterParentheses(s)
print(out)        
        