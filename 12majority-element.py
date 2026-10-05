class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums:
            count=nums.count(i)
            
            if count >len(nums)//2:
                return i
         
        
nums= list(map(int,input('enter elements: ').split()))

out=Solution()

output = out.majorityElement(nums)
print(output)        