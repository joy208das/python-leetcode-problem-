class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        a=0
        for i in range(0,len(nums)):
            if nums[i]!=val:
                nums[a]=nums[i]
                a=a+1
                
        return a 
         
        
        
nums= list(map(int,(input('enter elements: ').split())))
val= int(input('enter target value: '))   

p= Solution()   

r=p.removeElement(nums,val)
print(r)
