class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        b = 0
        x = len(nums)
        
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif target > nums[i]:
                b = i + 1
        
        return b

# Input
nums = list(map(int, input('Enter elements: ').split()))
target = int(input('Enter target: '))


p = Solution()
a = p.searchInsert(nums, target)
print(a)
