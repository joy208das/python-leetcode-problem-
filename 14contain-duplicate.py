# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
        
#         for i in nums:
#             b=nums.count(i)
#             if b>1:
#                 return True
            
            
            
#         return False
                    
        
        
        
# nums = list(map(int,input('enter ele:').split()))

# out=Solution()
# output=out.containsDuplicate(nums)
# print(output)        

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()  # Set to track the numbers we've seen
        for num in nums:
            if num in seen:
                return True  # Duplicate found
            seen.add(num)  # Add the number to the set
        return False  # No duplicates found

# Example usage
nums = list(map(int, input('Enter elements: ').split()))

out = Solution()
output = out.containsDuplicate(nums)
print(output)
