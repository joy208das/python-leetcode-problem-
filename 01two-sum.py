class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found

# Taking input from the user
nums = list(map(int, input("Enter the numbers in the array, separated by spaces: ").split()))
target = int(input("Enter the target value: "))

# Creating an instance of the Solution class
solution = Solution()

# Finding the indices of the two numbers that add up to the target
result = solution.twoSum(nums, target)

# Printing the result
if result:
    print(f"The indices of the two numbers that add up to {target} are: {result}")
else:
    print(f"No two numbers in the array add up to {target}")

