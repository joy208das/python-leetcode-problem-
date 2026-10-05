class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s)!=len(t):
            return False
        
        first = ''.join(sorted(s))
        second = ''.join(sorted(t))
        
        if first == second:
            return True
        
        
        
s=input('enter 1st one:')
t=input('enter 2nd one:')

out =Solution()
output = out.isAnagram(s,t)
print(output)        