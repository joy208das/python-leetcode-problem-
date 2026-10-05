class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a=[]
        b=[]
        
        for i in range(len(s)):
            if s[i]=='#' and len(a)>0:
                a.pop()
            elif s[i]!='#':
                a.append(s[i])  
                  
        for j in range(len(t)):
            if t[j]=='#'and len(b)>0:
                b.pop()
            elif t[j]!='#':
                b.append(t[j])  
        if a==b:
            return True     
        
s = list(map(str,input('enter 1st: ').split()))
t =  list(map(str,input('enter 2nd: ').split()))       

out = Solution()

ou = out.backspaceCompare(s,t)
print(ou)