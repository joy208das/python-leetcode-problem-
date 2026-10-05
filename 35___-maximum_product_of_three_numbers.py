'''
[-100,-98,0,1,2,4]

maximum three product is -100,-98,4
their multiplication is -100*-98*4

'''
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        nums.sort()
        a= max((nums[-1]*nums[-2]*nums[-3]),(nums[0]*nums[1]*nums[-1]))
        return a
    
nums = list(map(int,input().split()))    
ou=Solution()
out=ou.maximumProduct(nums)
print(out)