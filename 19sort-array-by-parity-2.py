class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even = 0
        odd = 1
        n= len(nums)
        while even< n and odd<n:
            if nums[even]%2!=0:
                nums[even],nums[odd]=nums[odd],nums[even]
                odd+=2
            else:
                even+=2
                
        return nums                 
        
        
nums = list(map(int,input('enter elements: ').split()))    
out =Solution()
output=out.sortArrayByParityII(nums)
print(output)     