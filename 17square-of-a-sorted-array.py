class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list = []
        for i in nums:
            list.append(i**2)
        list.sort()  
        
        return list
nums = list(map(int,input('enter elements: ').split()))    
out =Solution()
output=out.sortedSquares(nums)
print(output)