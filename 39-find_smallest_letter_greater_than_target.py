class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        if target<self.kam(letters,target):
            return self.kam(letters,target)
        else :
            return letters[0]
        
    def kam(self,letters,target):
            l=0
            e=len(letters)-1
            m=(l+e)//2
            ans=-1
            while l<=e :
                if letters[m]>target:
                    ans= m
                    e=m-1
                
                else :
                    l=m+1
                    
                m=(l+e)//2
                
            return letters[ans]  
        
        
        
        
        
        
nums = list(map(str,input('enter elements: ').split()))    
target= input('enter targert:')
out =Solution()
output=out.nextGreatestLetter(nums,target)
print(output)           