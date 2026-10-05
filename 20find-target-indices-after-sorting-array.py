class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        t=[]
        for i in range(len(nums)):
            if nums[i]==target:
               t.append(i)
               continue
        return t    
        
        
        
nums = list(map(int,input('enter elements: ').split())) 
target=int(input('enter target element: '))   
out =Solution()
output=out.targetIndices(nums,target)
print(output)         