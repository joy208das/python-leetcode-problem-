class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0  # Duplicate count
        a = len(nums)  # Size of the original list
        
        # We will maintain a separate index to move the unique elements.
        unique_index = 0
        
        for i in range(1, a):
            if nums[i] != nums[unique_index]:  # Check if current element is different from the last unique one
                unique_index += 1  # Move the unique index forward
                nums[unique_index] = nums[i]  # Place the next unique element at the unique_index position
        
        # The number of unique elements will be (unique_index + 1), 
        # because unique_index is zero-based.
        return unique_index + 1

# Example usage
nums = list(map(int, input('Enter elements: ').split()))  # Input list of integers

p = Solution()
re = p.removeDuplicates(nums)  # Remove duplicates and get the count of unique elements

print(re)  # Prints the number of unique elements
print(nums[:re])  # Prints the modified array with only unique elements
