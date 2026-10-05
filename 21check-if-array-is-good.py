class Solution(object):
    def isGood(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        arr=0
        a=len(nums)
        for i in range(len(nums)):
            if nums[i]>arr:
                arr=nums[i]
                
        return  arr+1==a
            
        
nums = list(map(int,input('enter elements: ').split()))    
out =Solution()
output=out.isGood(nums)
print(output)     
        
           