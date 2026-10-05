class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        au = list(s)
        stack=[]
        
        for i in range(len(au)):
            if stack and ((stack[-1]=='A' and au[i]=='B') or (stack[-1]=='C' and au[i]=='D')):
                stack.pop()
            else:
                stack.append(au[i])
         
        return len(stack)            
        
        
s=input('enter: ')
ou = Solution()
out= ou.minLength(s)
print(out)        

'''https://leetcode.com/problems/minimum-string-length-after-removing-substrings/description/'''