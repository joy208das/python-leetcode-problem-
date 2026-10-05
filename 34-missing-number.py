class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = len(nums)  
        nums.sort()
        
        for i in range(a + 1):  
            a = self.kam(i, nums)  
            if not a:  
                return i

    def kam(self, i, nums):
        l = 0
        e = len(nums) - 1
        m=(l+e)//2
        while l <= e: 
            
            if nums[m] == i:  
                return True
            elif nums[m] > i: 
                e = m - 1
            else:  
                l = m + 1
            m=(l+e)//2
            
        return False  
    
# Example usage
if __name__ == "__main__":
    nums = list(map(int, input('Enter numbers separated by space: ').split()))
    solution = Solution()
    missing_number = solution.missingNumber(nums)
    print(f"The missing number is: {missing_number}")
