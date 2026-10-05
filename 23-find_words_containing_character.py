class Solution(object):
    def findWordsContaining(self, words, x):
        """
        :type words: List[str]
        :type x: str
        :rtype: List[int]
        """
        a=[]
        for i,word in enumerate(words):
            if x in word:
                a.append(i)
           
        return a        
                
        
       
        
        
words = list(map(str,input('enter your words: ').split())) 
x= input('enter target letter: ')

out = Solution()
output=out.findWordsContaining(words,x)

print(output)

       