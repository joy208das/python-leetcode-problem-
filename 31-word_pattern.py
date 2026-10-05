class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        a=list(map(str,pattern))
        b=list(map(str,s))
        x=0
        y=0
        if len(a)%2!=0 or len(b)%2!=0 :
            return False
        self.kam(a,x)
        self.kam(b,y)
        if x==y:
            return True
        
        
    def kam(self,n,t):
        foyla=[]
        dui=[]
        for i in  range(0,len(n)/2):
            foyla.append(n[i]) 
            
        for j in range(len(n)-1,(len(n)/2)-1,-1) :
            dui.append(n[j])
        
        if foyla == dui :
            t=t+1
            
        return t        
        
p=input('enter pattern: ')
s=input('enter s: ')

ou=Solution()
out = ou.wordPattern(p,s)
print(out)        
'''https://leetcode.com/problems/word-pattern/description/'''