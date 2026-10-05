class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        x=list(map(str,word))
        a=[]
        for i in range(len(x)):
            if x[i]==ch:
                for j in range(i,-1,-1):
                    a.append(x[j])
                for k in range(i+1,len(x)):
                    a.append(x[k])    
                break  
            if ch not in x:
                return word
            
        return "".join(map(str,a))            
        
word = input('enter your word: ')
ch = input('enter ch: ')

ou= Solution()
out = ou.reversePrefix(word,ch)
print(out)        