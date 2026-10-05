'''we can learn about isdigit()
'''

class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        b=list(map(str,s))
        j=len(b)
        a=[]
        
     
        for i in range(j):
            if b[i].isdigit():# Check if the current character is a digit
                a.pop()
                
            else:
                a.append(s[i])           
        
        return "".join(map(str,a))       
                
nums = input('enter: ')   
out =Solution()
output=out.clearDigits(nums)
print(output)     